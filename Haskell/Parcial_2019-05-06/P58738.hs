data STree a = Nil | Node Int a (STree a) (STree a) deriving Show

talla :: STree a -> Int
talla Nil = 0
talla (Node t _ _ _) = t

isOk :: STree a -> Bool
isOk Nil = True
isOk (Node t _ l r) = (isOk l) && (isOk r) && (t == (talla l) + (talla r) + 1)

nthElement :: STree a -> Int -> Maybe a
nthElement (Node t x l r) n
    | n > t || n < 1 = Nothing
    | n <= tl = nthElement l n
    | n == tl + 1 = Just x
    | otherwise = nthElement r (n - tl - 1)
        where
            tl = talla l

mapToElements :: (a -> b) -> STree a -> [Int] -> [Maybe b] 
mapToElements f t n = map apply n
    where 
        apply nE = do
            el <- nthElement t nE
            return $ f el



div10 = flip div 10
t1 = Node 3 99 (Node 1 88 Nil Nil) (Node 1 22 Nil Nil)
t2 = Node 2 77 (Node 1 33 Nil Nil) Nil
t3 = Node 6 44 t1 t2
t4 = Node 7 55 t1 t2

instance Functor STree where
    fmap f Nil = Nil
    fmap f (Node t x l r) = Node t (f x) (fmap f l) (fmap f r)