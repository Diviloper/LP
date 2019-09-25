myMap :: (a -> b) -> [a] -> [b]
myMap f m = [f x | x <- m]

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f m = [x | x <- m, f x]

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f m n = [f x y | (x, y) <- zip m n]

thingify :: [Int] -> [Int] -> [(Int, Int)]
thingify m n = [(x, y) | x <- m, y <- n, mod x y == 0]

factors :: Int -> [Int]
factors x = [y | y <- [1..x], mod x y == 0]