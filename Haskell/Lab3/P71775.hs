countIf :: (Int -> Bool) -> [Int] -> Int
countIf p x = length $ filter p x

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam m fs = map (flip map m) fs

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 m fs = map (\x -> [f x | f <- fs]) m

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl p f x m = foldl f x $ filter p m

insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert p [] x = [x]
insert p (m:ms) x 
    | p m x = m : insert p ms x
    | otherwise = [x, m] ++ ms

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort p ms = foldl (insert p) [] ms