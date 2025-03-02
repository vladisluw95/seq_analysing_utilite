from abc import ABC, abstractmethod


class NucleotideError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class ProteinError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class BiologicalSequence(ABC):
    @abstractmethod
    def len_seq(self):
        return (f"length of sequence is {len(self)}")

    def nuc_ind(self, index: int, start: int, stop: int, step: int):
        print(self[index])
        print(self[start:stop:step])

    def nuc_str(self):
        print(f"your sequence {str(self)}")

    def nuc_corct(self):   
        if 'U' in self.upper.split():
            print('your sequence is RNA')
        elif 'T' in self.upper.split():
            print('your sequence is DNA')
        elif 'U' & 'T' in self.upper.split():
            return NucleotideError('It is impossible, check yor data!')


class NucleicAcidSequence:
    def __init__(self, sequence: str):
        self.sequence = sequence.upper()

    def complement(self):
        complimentary_rules_DNA = {
            'A': 'T',
            'G': 'C',
            'T': 'A',
            'C': 'G',
            'a': 't',
            'g': 'c',
            't': 'a',
            'c': 'g'
        }

        complimentary_rules_RNA = {
            'A': 'U',
            'G': 'C',
            'U': 'A',
            'C': 'G',
            'a': 'u',
            'g': 'c',
            'u': 'a',
            'g': 'c'
        }
        if 'U' in self.sequence:
            rules = complimentary_rules_RNA
        else:
            rules = complimentary_rules_DNA

        result = []
        for nucleotide in self.sequence:
            if nucleotide in rules:
                result.append(rules[nucleotide])
            else:
                raise NucleotideError(f"It is impossible, check your data!")
        return ''.join(result)

    def reverse(self):
        return self.sequence[::-1]

    def reverse_complement(self):
        return self.complement()[::-1]


class DNASequence(NucleicAcidSequence):
    def transcribe(self: str):
        transcribtion_rules_DNA = {
            'A': 'A',
            'G': 'G',
            'T': 'U',
            'C': 'C',
            'a': 'a',
            'g': 'g',
            't': 'u',
            'c': 'c'
        }
        rules = transcribtion_rules_DNA
        return "".join([rules[c] for c in self.sequence])


class RNASequence(NucleicAcidSequence):
    def transcribe(self: str):
        transcribtion_rules_RNA = {
            'A': 'A',
            'G': 'G',
            'U': 'T',
            'C': 'C',
            'a': 'a',
            'g': 'g',
            'u': 't',
            'c': 'c'   
            }
        rules = transcribtion_rules_RNA
        return "".join([rules[c] for c in self.sequence])


class AminoAcidSequence(BiologicalSequence):
    def __init__(self, sequence: str):
        self.sequence = sequence.upper()

    def len_seq(self):
        return (f"length of protein is {len(self)}")

    def aa_to_names(self):
        amino_acids = {
            'A': 'Alanine',
            'R': 'Arginine',
            'N': 'Asparagine',
            'D': 'Aspartic acid',
            'C': 'Cysteine',
            'Q': 'Glutamine',
            'E': 'Glutamic acid',
            'G': 'Glycine',
            'H': 'Histidine',
            'I': 'Isoleucine',
            'L': 'Leucine',
            'K': 'Lysine',
            'M': 'Methionine',
            'F': 'Phenylalanine',
            'P': 'Proline',
            'S': 'Serine',
            'T': 'Threonine',
            'W': 'Tryptophan',
            'Y': 'Tyrosine',
            'V': 'Valine'}

        aa_names = []
        for am in self.sequence:
            if am in amino_acids:
                aa_names.append(amino_acids[am])
            else:
                raise ProteinError('It is impossible, check your data!')
        return ','.join(aa_names)
