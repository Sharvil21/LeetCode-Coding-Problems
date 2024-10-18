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
