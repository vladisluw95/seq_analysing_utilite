
# `seq_analysing_utilite`
Here I present my first bioinformatics utility. This utility has four functions that work with DNA and RNA sequences, including FASTA and BLAST output files

# Functions in seq_analysing_utilite.py

## `run_dna_rna_tools()`
The run_dna_rna_tools function allows users to perform various operations on DNA or RNA sequences. The function accepts a variable number of sequence strings as input, followed by the operation to be performed.

### Arguments:
*args: The function takes any number of string arguments representing nucleotide sequences followed by the name of the operation.
Sequences should either be RNA or DNA but not a mix of both (e.g., a sequence containing both T and U will return an error).
Available operations are:
* **transcribe**
* **complement**
* **reverse**
* **reverse_complement**
* **gc_cont**
### Returns:
A string or a list of strings, depending on the number of sequences passed as input.
### Example:
``` run_dna_rna_tools("ATG", "TAC", "complement")``` 
### Output:
``` ['TAC', 'ATG']``` 

## `filter_fastq()`
The filter_fastq function is designed to filter sequences based on several criteria such as GC content, sequence length, and quality scores. The function expects a dictionary of sequences in FASTQ format and performs filtering based on the provided or default parameters.

### Arguments:

* **gc_bounds**
* **length_bounds**
* **quality_threshold**
## Returns:
A dictionary of sequences that meet all specified filtering criteria.
### Example:
```
input_fastq = os.path.join("example_fastq.fastq") # You need to write your path to file
output_fastq = os.path.join("output_fastq.fastq") # You need to write your path to file
filter_fastq(input_fastq,output_fastq)
``` 
### Output:
`output_fastq.fastq`


# Functions in bio_files_processor.py

## `bio_files_processor()`
Processes a FASTA file and extracts nucleotide sequences while excluding headers.
Writes the sequences to a new output file.
The bio_files_processor function reads a FASTA file, removes header lines (lines starting with '>'), and writes the nucleotide sequences to a new file.

### Example:

```input_fasta = os.path.join("example_multiline_fasta.fasta")# You need to write your path to file
output_fasta = os.path.join("output_fasta.fasta")# You need to write your path to file
bio_files_processor(input_fasta)
```
### Output:
`output_fasta.fasta`


## `parse_blast_output()`

Processes a BLAST output file to extract protein descriptions. Sorts the proteins in alphabetical order and saves them to an output file.

### Example:

```input_file = os.path.join("example_blast_results.txt") # You need to write your path to file
output_file = os.path.join("output_file.fasta") # You need to write your path to file
parse_blast_output(input_file)
```
### Output:
`output_file.txt`
