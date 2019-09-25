myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl f x [] = x
myFoldl f x (m:ms) = myFoldl f (f x m) ms

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr f x [] = x
myFoldr f x (m:ms) = f m (myFoldr f x ms)

myIterate :: (a -> a) -> a -> [a]
myIterate f x = x : myIterate f (f x)

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil p f x 
    | p x = x
    | otherwise = myUntil p f (f x)

myMap :: (a -> b) -> [a] -> [b]
myMap f m = [f x | x <- m]

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f m = [x | x <- m, f x]

myAll :: (a -> Bool) -> [a] -> Bool
myAll p m = and $ myMap p m

myAny :: (a -> Bool) -> [a] -> Bool
myAny p m = or $ myMap p m

myZip :: [a] -> [b] -> [(a, b)]
myZip x [] = []
myZip [] x = []
myZip (x:xs) (y:ys) = (x, y) : myZip xs ys

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f x y = myMap (uncurry f) (myZip x y)