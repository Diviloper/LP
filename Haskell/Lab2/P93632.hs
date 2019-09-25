eql :: [Int] -> [Int] -> Bool
eql x y 
    | length x /= length y = False
    | otherwise = and z
    where
        z = zipWith (==) x y

prod :: Num a => [a] -> a
prod = foldr (*) 1 

prodOfEvens :: [Int] -> Int
prodOfEvens = prod . (filter even)

powersOf2 :: [Int]
powersOf2 = iterate (* 2) 1

suma :: Num a => [a] -> a 
suma = foldr (+) 0

scalarProduct :: [Float] -> [Float] -> Float
scalarProduct x y = suma $ zipWith (*) x y