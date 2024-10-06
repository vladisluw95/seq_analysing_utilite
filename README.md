# seq_analysing_utilite
Here I present my first bioinformatics utility. This utility has two main functions that work with DNA and RNA sequences

# Functions
## run_dna_rna_tools()
The run_dna_rna_tools function allows users to perform various operations on DNA or RNA sequences. The function accepts a variable number of sequence strings as input, followed by the operation to be performed.

### Arguments:
*args: The function takes any number of string arguments representing nucleotide sequences followed by the name of the operation.
Sequences should either be RNA or DNA but not a mix of both (e.g., a sequence containing both T and U will return an error).
Available operations are:
* **transcribe**: Converts a DNA sequence into its RNA equivalent.
* **complement**: Returns the complementary sequence.
* **reverse**: Reverses the sequence.
* **reverse_complement**: Returns the reverse complement.
* **gc_cont**: Computes the GC content of the sequence.
### Returns:
A string or a list of strings, depending on the number of sequences passed as input.
## Example:
run_dna_rna_tools("ATG", "TAC", "complement")
### Output:
['TAC', 'ATG']

## filter_fastq()
The filter_fastq function is designed to filter sequences based on several criteria such as GC content, sequence length, and quality scores. The function expects a dictionary of sequences in FASTQ format and performs filtering based on the provided or default parameters.

### Arguments:
* **seqs**: A dictionary where each key is the FASTQ identifier, and each value is a tuple containing the nucleotide sequence and the associated quality string.
*params: Optional keyword arguments for specifying bounds:
* **gc_bounds**: A tuple defining the minimum and maximum acceptable GC content (default: (0.0, 100.0)).
* **length_bounds**: A tuple defining the minimum and maximum sequence length (default: (0, 2**32)).
* **quality_threshold**: The minimum quality score (default: 0).
## Returns:
A dictionary of sequences that meet all specified filtering criteria.
## Example:
filter_fastq(seqs, gc_bounds=(30.0, 70.0), length_bounds=(50, 150), quality_threshold=20))
### Output:
{'@SRX079801': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'), '@SRX079802': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'), '@SRX079803': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD'), '@SRX079804': ('TGAAGCGTCGATAGAAGTTAGCAAACCCGCGGAACTTCCGTACATCAGACACATTCCGGGGGGTGGGCCAATCCATGATGCCTTTG', 'FF@FFBEEEEFFEFFD@EDEFFB=DFEEFFFE8FFE8EEDBFDFEEBE+E<C<C@FFFFF;;338<??D:@=DD:8DDDD@EE?EB'), '@SRX079805': ('TAGGGTTGTATTTGCAGATCCATGGCATGCCAAAAAGAACATCGTCCCGTCCAATATCTGCAACATACCAGTTGGTTGGTA', '@;CBA=:@;@DBDCDEEE/EEEEEEF@>FBEEB=EFA>EEBD=DAEEEEB9)99>B99BC)@,@<9CDD=C,5;B::?@;A'), '@SRX079806': ('CTGCCGAGACTGTTCTCAGACATGGAAAGCTCGATTCGCATACACTCGCTGAGTAAGAGAGTCACACCAAATCACAGATT', 'E;FFFEGFGIGGFBG;C6D<@C7CDGFEFGFHDFEHHHBBHHFDFEFBAEEEEDE@A2=DA:??C3<BCA7@DCDEG*EB'), '@SRX079807': ('CATTATAGTAATACGGAAGATGACTTGCTGTTATCATTACAGCTCCATCGCATGAATAATTCTCTAATATAGTTGTCAT', 'HGHHHHGFHHHHFHHEHHHHFGEHFGFGGGHHEEGHHEEHBHHFGDDECEGGGEFGF<FGGIIGEBGDFFFGFFGGFGF'), '@SRX079808': ('GACGCCGTGGCTGCACTATTTGAGGCACCTGTCCTCGAAGGGAAGTTCATCTCGACGCGTGTCACTATGACATGAATG', 'GGGGGFFCFEEEFFDGFBGGGA5DG@5DDCBDDE=GFADDFF5BE49<<<BDD?CE<A<8:59;@C.C9CECBAC=DE'), '@SRX079810': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC', 'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE'), '@SRX079811': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA', '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'), '@SRX079812': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG', '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')}

