import os.path
from typing import Dict, Union, List, Tuple



from utilites.nucleotides_act import transcribe, complement, reverse, reverse_complement, gc_cont
from utilites.filtering import gc_bounds_mod, length_bounds_mod, quality_threshold_mod


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


def filter_fastq(input_fastq:str,
                 output_fasta: str,
                 gc_bounds: Tuple[float,float] = (0.0, 100.0),
                 length_bounds:Tuple[int,int] = (0, 2**32),
                 quality_threshold: float = 0.0) -> None:
    """
    filter_fastq takes as input an file in fastq format for analysing nucleotides sequences.
    filter_fastq returns result of analysing to output_fast.fastq/

    Args
    input_fastq (str) path to the input fasta file with a raw data of the sequensing
    And params for func from
    gc_bounds
    length_bounds
    quality_threshold

    Return value:
    The function does not return any values but creates a file with result of analysing of sequences.
    """
    fastq_data = {}
    with open(input_fastq,"r") as fastq:
        while True:
            header = fastq.readline()
            if not header:
                break
            sequence = fastq.readline()
            fastq.readline()
            quality = fastq.readline()
            fastq_data[header] = (sequence, quality)

    result = {}
    gc_bounds = (0.0, 100.0) if gc_bounds is None else gc_bounds
    length_bounds = (0, 2**32) if length_bounds is None else length_bounds
    quality_threshold = (0.0) if quality_threshold is None else quality_threshold

    gc_res = gc_bounds_mod(fastq_data)
    length_res = length_bounds_mod(fastq_data)
    quality_res = quality_threshold_mod(fastq_data, quality_threshold)

    for key, (sequence, quality) in fastq_data.items():
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

    with open(output_fasta,"w") as fastq:
        for header,(sequence,quality) in result.items():
                fastq.write(header + "\n" + sequence + "\n+\n" + quality+ "\n")

input_fastq = os.path.join("example_fastq.fastq")
output_fasta = os.path.join("output_fastq.fasta")
filter_fastq(input_fastq,output_fasta)
