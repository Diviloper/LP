analyze :: Int -> Either Int Bool
analyze x 
    | numDivs > 12 = Left numDivs
    | otherwise = Right $ potsumar divs 0 x
    where
        divs = getDivs x
        numDivs = length divs


getDivs :: Int -> [Int]
getDivs 1 = []
getDivs n
    | sqr == (fromIntegral sqrInt) = halfDivs ++ (tail $ reverse $ map (div n) (tail halfDivs))
    | otherwise = halfDivs ++ (reverse $ map (div n) (tail halfDivs))
    where
        sqr = sqrt $ fromIntegral n
        sqrInt = floor sqr
        halfDivs = [y | y <- [1.. sqrInt], mod n y == 0]


potsumar :: [Int] -> Int -> Int -> Bool
potsumar [] current target = current == target
potsumar (now:nums) current target
    | current == target = True
    | potsumar nums current target = True
    | otherwise = potsumar nums (current + now) target 