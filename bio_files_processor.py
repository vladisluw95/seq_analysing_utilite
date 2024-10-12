import os.path


def bio_files_processor(input_fasta: str):
    """
    The bio_files_processor function processes a fasta file
    and writes the nucleotide sequences to a new output file.

    Arguments:
    input_fasta (str): Path to the input fasta file containing sequences with headers.

    Return value:
    The function does not return any values but creates a file with sequences excluding headers.
    """

    sequence = []
    with open(input_fasta) as fasta:
        for line in fasta:
            if line.startswith(">"):
                continue
            else:
                sequence.append(line)
    with open(output_fasta, "w") as fasta:
        for seq in sequence:
            fasta.write(seq + "\n")


def parse_blast_output(input_file: str):
    """
    The parse_blast_output function processes a BLAST output file.


    Arguments:
    input_file (str): Path to the input BLAST output file containing information from BLAST by QUERY order.

    Return value:
    The function does not return any values but creates a file with list of proteins in alphabetical order.
    """
    proteins = []
    with open(input_file, "r") as file:
        lines = file.readlines()
        for line in range(len(lines)-1):
            if lines[line].startswith("Description"):
                proteins.append(lines[line + 1].strip())
        proteins.sort()
    with open(output_file, "w") as file:
        for p in proteins:
            file.write(p + "\n")


input_file = os.path.join("example_blast_results.txt")
output_file = os.path.join("output_file.txt")
input_fasta = os.path.join("example_multiline_fasta.fasta")
output_fasta = os.path.join("output_fasta.fasta")
parse_blast_output(input_file)
