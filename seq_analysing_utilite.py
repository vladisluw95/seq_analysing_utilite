from utilites.module1 import transcribe, complement, reverse, reverse_complement, gc_cont
from utilites.module2 import seqs, gc_bounds_12, length_bounds_12, quality_threshold_12
from typing import Dict, Union, Tuple, List


def run_dna_rna_tools(*args: Union[str, str]) -> Union[str, List[str]]:
    """
    run_dna_rna_tools takes as input seq and operations for analysing and doing some actions with nucleotides.

    Args
    seq is a any str. You can use any count of seq and choose either upper or lower cases.
    seq must be a DNA or RNA sequence. if you will use T and U in the same seq, run_dna_rna_tools gives you an error.
    operation is an actions for seq.
    operation must be "transcribe", "complement", "reverse", "reverse_complement" or "gc_cont". Otherwise run_dna_rna_tools backs with the error.

    Returns
    [str] of nucleotide after operations.
    """

    seq = args[:-1]
    operation = args[-1]
    dna_tools_res = []
    for s in seq:
        if ("T" in s or "t" in s) and ("U" in s or "u" in s):
            return "Error"
    if operation == "transcribe":
        fn = transcribe
    elif operation == "complement":
        fn = complement
    if operation == "reverse":
        fn = reverse
    elif operation == "reverse_complement":
        fn = reverse_complement
    elif operation == "gc_cont":
        fn = gc_cont
    for s in seq:
        result = fn(s)
        dna_tools_res.append(result)
    return dna_tools_res if len(dna_tools_res) > 1 else dna_tools_res[0]


def filter_fastq(seqs: Dict[str, Tuple[str, str]], **params) -> Dict[str, tuple[str, str]]:
    """
    filter_fastq takes as input a dict with fastq as keys, sequence as a value[0], phred code as a value[1] and operations for analysing of fastq in dict.

    Args
    seqs are dict named as seqs in module2.py
    **params are operations for analysing fastq from seqs

    Returns
    Dict of fastqs that suit for conditionals in operation.
    """
    result = {}
    if params.get("gc_bounds") is None:
        gc_bounds = (0.0, 100.0)
    else: gc_bounds = params.get("gc_bounds")
    if params.get("quality_threshold") is None:
        quality_threshold = 0
    else: quality_threshold = params.get("quality_threshold")
    if params.get("length_bounds") is None:
        length_bounds = (0, 2**32)
    else: length_bounds = params.get("length_bounds")

    gc_res = gc_bounds_12(seqs)
    length_res = length_bounds_12(seqs)
    quality_res = quality_threshold_12(seqs)

    for key, (sequence, quality) in seqs.items():
        gc = gc_res.get(key)
        if gc is None or not (gc_bounds[0] <= gc <= gc_bounds[1]):
            continue
        length = length_res.get(key)
        if length is None or not (length_bounds[0] <= length <= length_bounds[1]):
            continue
        current_quality = quality_res.get(key)
        if current_quality is None or not (quality_threshold < current_quality):
            continue
        result[key] = (sequence, quality)
    return result
