-- Problema 1: Expressió postfixa 1

-- eval1 :: String -> Int
-- eval1 s = 

-- Problema 2: Expressió postfixa 2

eval2 :: String -> Int
eval2 s = head $ foldl manage [] $ words s
    where
        manage :: [Int] -> String -> [Int]
        manage (x:y:l) "+" = ((y+x):l)
        manage (x:y:l) "-" = ((y-x):l)
        manage (x:y:l) "*" = ((y*x):l)
        manage (x:y:l) "/" = ((div y x):l)
        manage l x = (read x) : l

-- Problema 3: fsmap

fsmap :: a -> [a -> a] -> a
fsmap v fs = foldl (flip ($)) v fs