ones :: [Integer]
ones = repeat 1

nats :: [Integer]
nats = iterate (+ 1) 0

ints :: [Integer]
ints = iterate createInts 0
    where
        createInts :: Integer -> Integer
        createInts x 
            | x > 0 = -x
            | otherwise = -x + 1

triangulars :: [Integer]
triangulars = scanl (+) 0 $ tail nats

factorials :: [Integer]
factorials = scanl (*) 1 $ tail nats

fibs :: [Integer]
fibs = f 0 1
    where
        f :: Integer -> Integer -> [Integer]
        f x y = x : (f y $ x + y)

primes :: [Integer]
primes = filter isPrime $ tail nats
    where
        isPrime :: Integer -> Bool
        isPrime 1 = False
        isPrime 2 = True
        isPrime n
            | even n = False
            | otherwise = isPrimeAux 3
            where
            isPrimeAux :: Integer -> Bool
            isPrimeAux d
                |d>= div n 2 = True
                |mod n d == 0 = False
                |otherwise = isPrimeAux (d + 2)

merge :: [Integer] -> [Integer] -> [Integer]
merge (x:xs) (y:ys)
    | x < y = x : merge xs (y:ys)
    | x == y = x : merge xs ys
    | otherwise = y : merge (x:xs) ys

hammings :: [Integer]
hammings = 1 : (merge (map (*2) hammings) $ merge (map (*3) hammings) (map (*5) hammings) )


lookNsay :: [Integer]
lookNsay = map (read) lookNsayStrings
    where
        lookNsayStrings :: [String]
        lookNsayStrings = iterate lookAndSay "1"
            where
                lookAndSay :: String -> String
                lookAndSay x = say $ look x
                    where
                        look :: String -> [String]
                        look [] = []
                        look x = primerConjunt : (look resta)
                            where
                                primerConjunt = takeWhile (== primer) x
                                resta = dropWhile (== primer) x
                                primer = head x
                        say :: [String] -> String
                        say [] = []
                        say (x:xs) = (show $ length x ) ++ [head x] ++ say xs

tartaglia :: [[Integer]]
tartaglia = iterate nextTartaglia [1]
    where
        nextTartaglia :: [Integer] -> [Integer]
        nextTartaglia x = zipWith (+) (0:x) (x++[0])
