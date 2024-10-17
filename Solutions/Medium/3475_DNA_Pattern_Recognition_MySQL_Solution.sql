--MySQL Solution
# Write your MySQL query statement below
SELECT
sample_id, dna_sequence, species,
SUM(CASE WHEN dna_sequence REGEXP '^ATG' THEN 1 ELSE 0 END) AS has_start,
SUM(CASE WHEN dna_sequence REGEXP '(TAA|TAG|TGA)$' THEN 1 ELSE 0 END) AS has_stop,
SUM(CASE WHEN dna_sequence REGEXP 'ATAT' THEN 1 ELSE 0 END) AS has_atat,
SUM(CASE WHEN dna_sequence REGEXP '(G{3}|G{4})' THEN 1 ELSE 0 END) AS has_ggg
FROM Samples
GROUP BY 1,2,3
ORDER BY 1
