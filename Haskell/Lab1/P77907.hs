absValue :: Int -> Int
absValue n
  | n<0 = (-n)
  | otherwise = n

power :: Int -> Int -> Int
power x p
  | p==0 = 1
  | even p = y * y
  | otherwise = y * y * x
  where
    y = power x p2
    p2 = div p 2

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

slowFib :: Int -> Int
slowFib n
  |n==0 = 0
  |n==1 = 1
  |otherwise = slowFib (n-1) + slowFib (n-2)

quickFib :: Int -> Int
quickFib n = fst (auxFib n)
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
    

