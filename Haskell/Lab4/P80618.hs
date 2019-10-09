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

