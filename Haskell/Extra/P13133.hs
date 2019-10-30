sumMultiples35 :: Integer -> Integer
sumMultiples35 n = sum [ x | x <- [1..n-1], (mod x 3) == 0 || (mod x 5) == 0]

fibonacci :: Int -> Integer
fibonacci n = fst (auxFib n)
    where
      auxFib :: Int -> (Integer, Integer)
      auxFib 0 = (0, 1)
      auxFib n 
        | even n = (f, f1)
        | otherwise = (f1, f + f1)
        where
          (a, b) = auxFib (div n 2)
          f = a * (b * 2 - a)
          f1 = a * a + b * b

sumEvenFibonaccis :: Integer -> Integer
sumEvenFibonaccis n = sum $ filter even $ takeWhile (< n) $ fibs' 0 1
  where
    fibs' m n = m : fibs' n (m+n)

largestPrimeFactor :: Int -> Int
largestPrimeFactor x = maximum $ filter isPrime $ factors x


isPalindromic :: Integer -> Bool
isPalindromic x = s == reverse s
  where
    s = show x




-- Helpers
isPrime :: Int -> Bool
isPrime 1 = False
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

factors :: Int -> [Int]
factors x = [y | y <- [1..x], mod x y == 0]