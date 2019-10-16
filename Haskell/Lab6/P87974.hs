main :: IO()
main = do
    name <- getLine
    let fem = last name == 'a' || last name == 'A' 
    if fem then putStrLn "Hola maca!" else putStrLn "Hola maco!"