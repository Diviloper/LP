myLength :: [Int] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs

myMaximum :: [Int] -> Int
myMaximum [x] = x
myMaximum (x:xs)
    | x < m = m
    | otherwise = x
    where
        m = myMaximum xs

average:: [Int] -> Float
average x = 
    s / l
    where
        s = fromIntegral (sum x) :: Float
        l = fromIntegral (myLength x) :: Float

buildPalindrome :: [Int] -> [Int]
buildPalindrome x = reverse x ++ x

remove :: [Int] -> [Int] -> [Int]
remove [] y = []
remove (x:xs) y
    | x `elem` y = remove xs y
    | otherwise = x : (remove xs y) 

flatten :: [[Int]] -> [Int]
flatten [] = []
flatten (x:xs) = x ++ (flatten xs)

oddsNevens :: [Int] -> ([Int], [Int])
oddsNevens [] = ([], [])
oddsNevens (x:xs)
    | even x = (f, x : s)
    | otherwise = (x : f, s)
    where
        f = fst p
        s = snd p
        p = oddsNevens xs

isPrime :: Int -> Bool
isPrime 2 = True
isPrime n
    | even n = False
    | otherwise = isPrimeAux 3
    where
    isPrimeAux :: Int -> Bool
    isPrimeAux d
        |d>= div n 2 = True
        |mod n d == 0 = False
        |otherwise = isPrimeAux (d + 2)

primeDivisors :: Int -> [Int]
primeDivisors x 
    | isPrime x = [x]
    | otherwise = primeDivs x 2
    where 
        primeDivs :: Int -> Int -> [Int]
        primeDivs x y
            | y > (div x 2) = []
            | ((mod x y) == 0) && (isPrime y) = y : primeDivs x (y+1)
            | otherwise = primeDivs x (y+1)
