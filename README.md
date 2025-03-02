# seq_analysing_utilite
Here I present my first bioinformatics utility. This utility was written by OOP structure. Here you can find tools for analysing biological sequences such as DNA, RNA and aminoacid. It includes functionality for sequence manipulation, transcription, complementation, and error handling for invalid sequences.

## Classes Overview

### 1. **Exceptions**
- `NucleotideError`: Raised when an invalid nucleotide sequence is encountered.
- `ProteinError`: Raised when an invalid protein sequence is encountered.

---

### 2. **Abstract Base Class**
- `BiologicalSequence`: An abstract base class that defines common methods for biological sequences.
  - `len_seq()`: Returns the length of the sequence.
  - `nuc_ind(index, start, stop, step)`: Prints the nucleotide at a specific index and a slice of the sequence.
  - `nuc_str()`: Prints the sequence as a string.
  - `nuc_corct()`: Checks if the sequence is DNA or RNA and raises an error if both 'U' and 'T' are present.

---

### 3. **Nucleic Acid Sequences**
- `NucleicAcidSequence`: A base class for DNA and RNA sequences.
  - `complement()`: Returns the complementary sequence.
  - `reverse()`: Returns the reversed sequence.
  - `reverse_complement()`: Returns the reverse complement of the sequence.

- `DNASequence`: Inherits from `NucleicAcidSequence` and adds a `transcribe()` method to transcribe DNA to RNA.
- `RNASequence`: Inherits from `NucleicAcidSequence` and adds a `transcribe()` method to transcribe RNA to DNA.

---

### 4. **Protein Sequences**
- `AminoAcidSequence`: Inherits from `BiologicalSequence` and provides methods for protein sequences.
  - `len_seq()`: Returns the length of the protein sequence.
  - `aa_to_names()`: Converts the protein sequence to a list of amino acid names.

---

### 5. **Installation**
- `git clone` [https://github.com/your-repo/seq_analysing_utilite.git](https://github.com/vladisluw95/seq_analysing_utilite.git)
- `cd` seq_analysing_utilite

---

### 6. Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

