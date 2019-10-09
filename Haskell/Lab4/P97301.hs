fizzBuzz :: [Either Int String]
fizzBuzz = [fizzBuzzValue x | x <- [0..]]
    where
        fizzBuzzValue :: Int -> Either Int String
        fizzBuzzValue x  
            | mod3 && mod5 = Right "FizzBuzz"
            | mod3 = Right "Fizz"
            | mod5 = Right "Buzz"
            | otherwise = Left x
                where
                    mod3 = mod x 3 == 0
                    mod5 = mod x 5 == 0