exps :: Float -> [Float]
exps x = zipWith (/) (iterate (*x) 1.0) (scanl (*) 1 [1..])

exponencial :: Float -> Float -> Float
exponencial x limit = sum $ takeWhile (>= limit) $ exps x