myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl f x [] = x
myFoldl f x (m:ms) = f (myFoldl f x ms) m

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr f x [] = x
myFoldr f x (m:ms) = f m (myFoldr f x ms)