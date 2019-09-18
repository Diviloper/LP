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
isPrime n
  | even n = False
  | n == 3 = False
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

