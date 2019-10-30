data Avi = Avi {
    nom :: [Char],
    edat :: Int,
    despeses :: [Int]
    } deriving (Show)

promigDespeses :: Avi -> Int
promigDespeses (Avi _ _ x) = round $ (sum $ map fromIntegral x) / (fromIntegral $ length x)

edatsExtremes :: [Avi] -> (Int, Int)
edatsExtremes x = (minimum ed, maximum ed)
    where
        ed = map (\(Avi _ e _) -> e) x

sumaPromig :: [Avi] -> Int
sumaPromig = sum . map promigDespeses

maximPromig :: [Avi] -> Int
maximPromig = maximum . map promigDespeses

despesaPromigSuperior :: [Avi] -> Int -> ([Char], Int)
despesaPromigSuperior l x = (n, e)
        where
            (Avi n e _) = head $ filter (\a -> promigDespeses a > x) (l ++ [(Avi "" 0 [x+1])])

avis = [ Avi { nom = "Joan", edat = 68, despeses = [640, 589, 573]}, Avi { nom = "Pepa", edat = 69, despeses = [710,550,570,698,645,512]}, Avi { nom = "Anna", edat = 72, despeses = [530,534]}, Avi { nom = "Pep", edat = 75, despeses = [770,645,630,650,590,481,602]} ]
