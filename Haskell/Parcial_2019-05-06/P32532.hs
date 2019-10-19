divisors :: Int -> [Int]
divisors x = [ y | y <- [1..x], mod x y == 0]

nbDivisors :: Int -> Int
nbDivisors = length . divisors

moltCompost :: Int -> Bool
moltCompost x = null petitsMesComposts
    where
        petitsMesComposts = [ y | y <- [1..(x-1)], (nbDivisors y) >= nbDivs]
        nbDivs = nbDivisors x