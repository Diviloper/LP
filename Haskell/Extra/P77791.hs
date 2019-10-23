serieCollatz :: Integer -> [Integer]
serieCollatz 1 = [1]
serieCollatz x 
    | mod x 2 == 0 = x : serieCollatz (div x 2)
    | otherwise = x : serieCollatz (x * 3 + 1)

collatzMesLlarga :: Integer -> Integer
collatzMesLlarga x = maximum $ map (toInteger . length . serieCollatz) [1..x]
