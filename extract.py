# This is file #1 in the Autism Project...
# After unzipping the dataset soft file, run the follwing cmds to get the dataset_full file
# The pre_CDA is the sam as the dataset_full with class labels instead of sample IDs.

# This is the terminal cmd used to get the header and convert it to list of strings.
# cmd -->  cat GDS4431_full.soft | head -369 | tail -1 | sed "s/\t/\", \"/g"
import pandas as pd

cases = ["GSM627135", "GSM627138", "GSM627139", "GSM627140", "GSM627141", "GSM627142", "GSM627143", "GSM627144", "GSM627145", "GSM627146", "GSM627147", "GSM627149", "GSM627150", "GSM627151", "GSM627152", "GSM627153", "GSM627154", "GSM627155", "GSM627156", "GSM627157", "GSM627158", "GSM627159", "GSM627160", "GSM627161", "GSM627162", "GSM627163", "GSM627164", "GSM627165", "GSM627166", "GSM627167", "GSM627168", "GSM627169", "GSM627170", "GSM627171", "GSM627172", "GSM627173", "GSM627175", "GSM627176", "GSM627178", "GSM627179", "GSM627180", "GSM627181", "GSM627182", "GSM627183", "GSM627184", "GSM627185", "GSM627186", "GSM627187", "GSM627188", "GSM627189", "GSM627190", "GSM627191", "GSM627192", "GSM627193", "GSM627194", "GSM627195", "GSM627196", "GSM627197", "GSM627198", "GSM627199", "GSM627200", "GSM627201", "GSM627202", "GSM627203", "GSM627204", "GSM627205", "GSM627206", "GSM627207", "GSM627208", "GSM627209", "GSM627210", "GSM627211", "GSM627212", "GSM627213", "GSM627214", "GSM627215", "GSM627216"]
controls = ["GSM627071", "GSM627072", "GSM627073", "GSM627074", "GSM627075", "GSM627076", "GSM627077", "GSM627078", "GSM627079", "GSM627080", "GSM627081", "GSM627082", "GSM627083", "GSM627084", "GSM627085", "GSM627086", "GSM627087", "GSM627088", "GSM627089", "GSM627090", "GSM627091", "GSM627092", "GSM627093", "GSM627094", "GSM627095", "GSM627096", "GSM627097", "GSM627098", "GSM627099", "GSM627100", "GSM627101", "GSM627102", "GSM627103", "GSM627104", "GSM627105", "GSM627106", "GSM627107", "GSM627108", "GSM627109", "GSM627110", "GSM627111", "GSM627112", "GSM627113", "GSM627114", "GSM627115", "GSM627116", "GSM627117", "GSM627118", "GSM627119", "GSM627120", "GSM627121", "GSM627122", "GSM627123", "GSM627124", "GSM627125", "GSM627126", "GSM627127", "GSM627128", "GSM627129", "GSM627130", "GSM627131", "GSM627132", "GSM627133", "GSM627134", "GSM627136", "GSM627137", "GSM627148", "GSM627174", "GSM627177"]
samples = cases + controls

dropped_col = ["ID_REF", "Gene title", "Gene symbol", "Gene ID", "UniGene title", "UniGene symbol", "UniGene ID", "Nucleotide Title", "GI", "GenBank Accession", "Platform_CLONEID", "Platform_ORF", "Platform_SPOTID", "Chromosome location", "Chromosome annotation", "GO:Function", "GO:Process", "GO:Component", "GO:Function ID", "GO:Process ID", "GO:Component ID"]

df = pd.read_csv('GDS4431_full.soft', delimiter='\t', header = 368, index_col='IDENTIFIER') # zero-indexing
#usecols=samples
df = df.drop(labels=dropped_col, axis=1).drop('--Control', axis=0).dropna(axis=0, how='all')
df.to_csv('dataset_full.txt', sep='\t')

df.columns = df.columns.map(lambda x: 1 if x in cases else 0, samples)
df.to_csv('pre_CDA.txt', sep='\t')

