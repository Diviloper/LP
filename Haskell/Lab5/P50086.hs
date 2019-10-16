data Queue a = Queue [a] [a]
    deriving (Show)
 
create :: Queue a
create = Queue [] []

push :: a -> Queue a -> Queue a
push n (Queue x y) = Queue x (n:y)

pop :: Queue a -> Queue a
pop (Queue [] []) = Queue [] []
pop (Queue [] x) = Queue (tail $ reverse x) []
pop (Queue x y) = Queue (tail x) y

top :: Queue a -> a
top (Queue [] x) = head $ reverse x
top (Queue x _) = head x

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty _ = False

instance Eq a => Eq (Queue a)
    where
        (Queue x y) == (Queue w z) = (x ++ (reverse y)) == (w ++ (reverse z))

-- Cua 2

instance Functor Queue
    where
        fmap f (Queue x y) = Queue (fmap f x) (fmap f y)

translation :: Num b => b -> Queue b -> Queue b
translation t = fmap (+t)

instance Applicative Queue
    where
        -- (<*>) :: f (a -> b) -> (f a -> f b)
        (Queue [] [f]) <*> q = (Queue [f] []) <*> q
        (Queue [f] []) <*> q = fmap f q
        pure x = Queue [x] []

instance Monad Queue
    where
        return x = Queue [x] []
        -- (>>=)  :: m a -> (a -> m b) -> m b
        (Queue x y) >>= f = foldl merge create (map f (x ++ (reverse y)))

merge :: Queue a -> Queue a -> Queue a
merge (Queue xf xs) (Queue yf ys) = Queue (xf ++ (reverse xs)) (yf ++ (reverse ys))

kfilter :: (p -> Bool) -> Queue p -> Queue p
kfilter f q = do
    v <- q
    if f v then return v else create

