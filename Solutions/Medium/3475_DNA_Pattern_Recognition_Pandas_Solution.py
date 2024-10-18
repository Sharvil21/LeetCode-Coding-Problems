#Pandas Solution
#Write the Pandas Query Below
import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples['has_start'] = samples['dna_sequence'].str.contains("^ATG").astype(int)
    samples['has_stop'] = samples['dna_sequence'].str.contains("(TAA|TAG|TGA)$").astype(int)
    samples['has_atat'] = samples['dna_sequence'].str.contains("ATAT").astype(int)
    samples['has_ggg'] = samples['dna_sequence'].str.contains("(G{4}|G{3})").astype(int)
    return samples

#Pandas Solution
SELECT sample_id,
       dna_sequence,
       species,
       dna_sequence ~ '^ATG'           AS has_start,
       dna_sequence ~ 'TAA$|TAG$|TGA$' AS has_stop,
       dna_sequence ~ '.*ATAT.*'       AS has_atat,
       dna_sequence ~ '.*GGG.*'        AS has_ggg
  FROM samples
 ORDER BY sample_id;
