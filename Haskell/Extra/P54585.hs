closest :: [(Float,Float)] -> Float
closest [p1, p2] = dist p1 p2
closest (x:xs) 
    | cx > cxs = cxs
    | otherwise = cx
        where
            cxs = closest xs
            cx = minimum [ dist x y | y <- xs]

dist :: (Float, Float) -> (Float, Float) -> Float
dist (x1, y1) (x2, y2) = sqrt ((x2 - x1)^2 + (y2 - y1)^2)