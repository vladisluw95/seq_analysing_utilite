from typing import Tuple, Dict


def gc_bounds_mod(seqs: Dict[str, Tuple[str, str]]) -> Dict[str, float]:
    result = {}
    for key, (sequence, quality) in seqs.items():
        gc = sequence.count("G") + sequence.count("C")
        gc_cont = gc / len(sequence) * 100
        result[key] = gc_cont
    return result


def length_bounds_mod(seqs: Dict[str, Tuple[str, str]]) -> Dict[str, int]:
    result = {}
    for key, (sequence, quality) in seqs.items():
        len_seq = len(sequence)
        result[key] = len_seq
    return result


def quality_threshold_mod(seqs: Dict[str, Tuple[str, str]], threshold: int) -> Dict[str, bool]:
    result = {}
    for key, (sequence, quality) in seqs.items():
        q_score = (sum(ord(q)-33 for q in quality)/len(quality))
        result[key] = q_score
    return result
