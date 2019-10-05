data Tree a = Node a (Tree a) (Tree a) | Empty 
    deriving (Show)

size :: Tree a -> Int
size Empty = 0
size (Node _ lc rc) = 1 + size lc + size rc

height :: Tree a -> Int
height Empty = 0
height (Node _ lc rc) = 1 + (max (height lc) (height rc))

equal :: Eq a => Tree a -> Tree a -> Bool 
equal Empty Empty = True
equal Empty _ = False
equal _ Empty = False
equal (Node a lca rca) (Node b lcb rcb) = a == a && (equal lca lcb) && (equal rca rcb)

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic Empty Empty = True
isomorphic Empty _ = False
isomorphic _ Empty = False
isomorphic (Node x lx rx) (Node y ly ry) = equal (Node x lx rx) (Node y ly ry) || equal (Node x lx rx) (Node y ry ly)

preOrder :: Tree a -> [a]
preOrder Empty = []
preOrder (Node a lc rc) = [a] ++ (preOrder lc) ++ (preOrder rc)

postOrder :: Tree a -> [a]
postOrder Empty = []
postOrder (Node a lc rc) = (postOrder lc) ++ (postOrder rc) ++ [a]

inOrder :: Tree a -> [a]
inOrder Empty = []
inOrder (Node a lc rc) = (inOrder lc) ++ [a] ++ (inOrder rc)

-- breadthFirst :: Tree a -> [a]

build :: Eq a => [a] -> [a] -> Tree a
build [] [] = Empty
build (h:pre) ind = Node h (build lpre lin) (build rpre rin)
    where
        lin = takeWhile (/= h) ind
        rin = tail $ dropWhile (/= h) ind
        lpre = takeWhile (/= (head rin)) pre
        rpre = dropWhile (/= (head rin)) pre

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap _ Empty x = x
overlap _ x Empty = x
overlap f (Node x lcx rcx) (Node y lcy rcy) = Node (f x y) (overlap f lcx lcy) (overlap f rcx rcy)


a1 :: Tree Int
a1 = Node 1 (Node 2 (Node 3 Empty Empty) Empty) (Node 4 Empty Empty)

a2 :: Tree Int
a2 = Node 5 (Node 1 (Node 2 Empty Empty) (Node 2 Empty Empty)) (Node 3 Empty Empty)

t7 = Node 7 Empty Empty
t6 = Node 6 Empty Empty
t5 = Node 5 Empty Empty
t4 = Node 4 Empty Empty
t3 = Node 3 t6 t7
t2 = Node 2 t4 t5
t1 = Node 1 t2 t3
t1' = Node 1 t3 t2