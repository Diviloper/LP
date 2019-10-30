import Data.List
import Data.Ord

votsMinim :: [([Char], Int)] -> Int -> Bool
votsMinim l m = or $ map (\(_, v) -> v < m) l

candidatMesVotat :: [([Char], Int)] -> [Char]
candidatMesVotat = fst . maximumBy (comparing snd)

votsIngressos :: [([Char], Int)] -> [([Char], Int)] -> [[Char]]
votsIngressos v i = filter (\x -> notElem x ic) vc
    where
        vc = map fst v
        ic = map fst i

rics :: [([Char], Int)] -> [([Char], Int)] -> [[Char]]
rics v i = map fst $ take 3 $ reverse $ sortBy (comparing snd) ic
    where
        ic = map addAst i
        vn = map fst v
        addAst :: ([Char], Int) -> ([Char], Int)
        addAst (nom, ing)
            | elem nom vn = (nom ++ "*", ing)
            | otherwise = (nom, ing)