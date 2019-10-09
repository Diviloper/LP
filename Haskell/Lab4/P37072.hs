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
equal (Node a lca rca) (Node b lcb rcb) = a == b && (equal lca lcb) && (equal rca rcb)

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic Empty Empty = True
isomorphic Empty _ = False
isomorphic _ Empty = False
isomorphic (Node x lx rx) (Node y ly ry) =  x == y && (((isomorphic lx ly) && isomorphic rx ry) || (isomorphic lx ry) && (isomorphic rx ly))

preOrder :: Tree a -> [a]
preOrder Empty = []
preOrder (Node a lc rc) = [a] ++ (preOrder lc) ++ (preOrder rc)

postOrder :: Tree a -> [a]
postOrder Empty = []
postOrder (Node a lc rc) = (postOrder lc) ++ (postOrder rc) ++ [a]

inOrder :: Tree a -> [a]
inOrder Empty = []
inOrder (Node a lc rc) = (inOrder lc) ++ [a] ++ (inOrder rc)

parents :: [Tree a] -> [a]
parents [] = []
parents l = map parent l
    where
        parent :: Tree a -> a
        parent (Node x _ _ ) = x

children :: [Tree a] ->  [Tree a]
children [] = []
children l = foldr (++) [] $ map getChildren l
    where 
        getChildren :: Tree a -> [Tree a]
        getChildren (Node a Empty Empty) = []
        getChildren (Node a x Empty) = [x]
        getChildren (Node a Empty x) = [x]
        getChildren (Node a x y) = [x,y]

breadthFirst :: Tree a -> [a]
breadthFirst Empty = []
breadthFirst a = breadthFirstAux [a]
        where 
            breadthFirstAux :: [Tree a] -> [a]
            breadthFirstAux [] = []
            breadthFirstAux l = parents l ++ (breadthFirstAux $ children l)

build :: Eq a => [a] -> [a] -> Tree a
build [] [] = Empty
build [x] [y] = Node x Empty Empty
build (h:pre) ind = Node h (build lpre lin) (build rpre rin)
    where
        lin = takeWhile (/= h) ind
        lastl = last lin
        rin = tail $ dropWhile (/= h) ind
        lpre = takeWhile (/= lastl) pre ++ [lastl]
        rpre = tail $ dropWhile (/= lastl) pre


overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap _ Empty x = x
overlap _ x Empty = x
overlap f (Node x lcx rcx) (Node y lcy rcy) = Node (f x y) (overlap f lcx lcy) (overlap f rcx rcy)



t7 = Node 7 Empty Empty
t6 = Node 6 Empty Empty
t5 = Node 5 Empty Empty
t4 = Node 4 Empty Empty
t3 = Node 3 t6 t7
t2 = Node 2 t4 t5
t1 = Node 1 t2 t3
t1' = Node 1 t3 t2