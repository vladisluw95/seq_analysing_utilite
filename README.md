# seq_analysing_utilite
Here I present my first bioinformatician utilite

##Functions
#1. run_dna_rna_tools
The run_dna_rna_tools function allows users to perform various operations on DNA or RNA sequences. The function accepts a variable number of sequence strings as input, followed by the operation to be performed.

###Arguments:
*args: The function takes any number of string arguments representing nucleotide sequences followed by the name of the operation.
Sequences should either be RNA or DNA but not a mix of both (e.g., a sequence containing both T and U will return an error).
Available operations are:
*transcribe: Converts a DNA sequence into its RNA equivalent.
*complement: Returns the complementary sequence.
*reverse: Reverses the sequence.
*reverse_complement: Returns the reverse complement.
*gc_cont: Computes the GC content of the sequence.
###Returns:
A string or a list of strings, depending on the number of sequences passed as input.
##Example:
run_dna_rna_tools("ATG", "TAC", "complement")
###Output:
['TAC', 'ATG']

#2. filter_fastq
The filter_fastq function is designed to filter sequences based on several criteria such as GC content, sequence length, and quality scores. The function expects a dictionary of sequences in FASTQ format and performs filtering based on the provided or default parameters.

###Arguments:
*seqs: A dictionary where each key is the FASTQ identifier, and each value is a tuple containing the nucleotide sequence and the associated quality string.
*params: Optional keyword arguments for specifying bounds:
*gc_bounds: A tuple defining the minimum and maximum acceptable GC content (default: (0.0, 100.0)).
*length_bounds: A tuple defining the minimum and maximum sequence length (default: (0, 2**32)).
*quality_threshold: The minimum quality score (default: 0).
##Returns:
A dictionary of sequences that meet all specified filtering criteria.
