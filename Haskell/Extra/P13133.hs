sumMultiples35 :: Integer -> Integer
sumMultiples35 n = sum [ x | x <- [1..n-1], (mod x 3) == 0 || (mod x 5) == 0]

fibonacci :: Int -> Int
fibonacci n = fst (auxFib n)
    where
      auxFib :: Int -> (Int, Int)
      auxFib 0 = (0, 1)
      auxFib n 
        | even n = (f, f1)
        | otherwise = (f1, f + f1)
        where
          (a, b) = auxFib (div n 2)
          f = a * (b * 2 - a)
          f1 = a * a + b * b

isPalindromic :: Integer -> Bool