
Here I present my first utility for bioinformatics. This utility was written based on an OOP framework. In it you will find tools for analysing biological sequences such as DNA, RNA and amino acids. It includes functionality for working with sequences, transcription, complementation and error handling for incorrect sequences, filtration of sequences in a fastq file. The programme consists of two parts: seq_analysing_utilite and filter_fastq.

Translated with DeepL.com (free version)
# seq_analysing_utilite
## Classes Overview

### 1.1 **Exceptions**
- `NucleotideError`: Raised when an invalid nucleotide sequence is encountered.
- `ProteinError`: Raised when an invalid protein sequence is encountered.

---

### 1.2 **Abstract Base Class**
- `BiologicalSequence`: An abstract base class that defines common methods for biological sequences.
  - `len_seq()`: Returns the length of the sequence.
  - `nuc_ind(index, start, stop, step)`: Prints the nucleotide at a specific index and a slice of the sequence.
  - `nuc_str()`: Prints the sequence as a string.
  - `nuc_corct()`: Checks if the sequence is DNA or RNA and raises an error if both 'U' and 'T' are present.

---

### 1.3 **Nucleic Acid Sequences**
- `NucleicAcidSequence`: A base class for DNA and RNA sequences.
  - `complement()`: Returns the complementary sequence.
  - `reverse()`: Returns the reversed sequence.
  - `reverse_complement()`: Returns the reverse complement of the sequence.

- `DNASequence`: Inherits from `NucleicAcidSequence` and adds a `transcribe()` method to transcribe DNA to RNA.
- `RNASequence`: Inherits from `NucleicAcidSequence` and adds a `transcribe()` method to transcribe RNA to DNA.

---

### 1.4 **Protein Sequences**
- `AminoAcidSequence`: Inherits from `BiologicalSequence` and provides methods for protein sequences.
  - `len_seq()`: Returns the length of the protein sequence.
  - `aa_to_names()`: Converts the protein sequence to a list of amino acid names.

---

## 1.5 **Requirements**

- Python 3.x

---

### 1.5 **Installation**
- `git clone` [https://github.com/your-repo/seq_analysing_utilite.git](https://github.com/vladisluw95/seq_analysing_utilite.git)
- `cd` seq_analysing_utilite

---

# 2.1 **filter fastq**
Function filters sequences in a FASTQ file based on length, quality, and GC content. It uses the `BioPython` library to handle FASTQ files and perform calculations.

---

## 2.2 **Features**

- **Filter by sequence length**: Specify minimum and maximum sequence lengths.
- **Filter by quality**: Set a minimum average quality score (Phred score).
- **Filter by GC content**: Define a range for GC content percentage.
---

## 2.3 **Requirements**

- Python 3.x
- [BioPython library](https://github.com/biopython/biopython.git)

---

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

