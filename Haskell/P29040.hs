insert :: [Int] -> Int -> [Int]
insert [] x = [x]
insert (x:xs) y
    | x < y = x : (insert xs y)
    | otherwise = y : x : xs

isort :: [Int] -> [Int]
isort [] = []
isort (x:xs) = insert (isort xs) x 

remove :: [Int] -> Int -> [Int]
remove [] y = []
remove (x:xs) y 
    | x == y = xs
    | otherwise = x : (remove xs y)

ssort :: [Int] -> [Int]
ssort [] = []
ssort x = m : y
    where 
        y = ssort (remove x m)
        m = minimum x

merge :: [Int] -> [Int] -> [Int]
merge [] [] = []
merge [] x = x
merge x [] = x
merge (x:xs) (y:ys) 
        | x < y = x : (merge xs (y:ys))
        | otherwise = y : (merge ys (x:xs))

msort :: [Int] -> [Int]
msort [] = []
msort [x] = [x]
msort x = merge (msort x1) (msort x2)
    where
        x1 = take l x
        x2 = drop l x
        l = div (length x) 2

qsort :: [Int] -> [Int]
qsort [] = []
qsort [x] = [x]
qsort (x:xs) = (qsort petits) ++ [x] ++ (qsort grans)
    where
        petits = [p | p <- xs, p < x]
        grans = [g | g <- xs, g >= x]

genQsort :: Ord a => [a] -> [a]
genQsort [] = []
genQsort [x] = [x]
genQsort (x:xs) = (genQsort petits) ++ [x] ++ (genQsort grans)
    where
        petits = [p | p <- xs, p < x]
        grans = [g | g <- xs, g >= x]