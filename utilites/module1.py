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


<<<<<<< HEAD
<<<<<<< HEAD
def transcribe(seq: list[str]):
=======
def transcribe(seq:List[str]):
>>>>>>> 8fa1609 (Add HW3 funcs to module1)
=======
def transcribe(seq: list[str]):
>>>>>>> 7606f0f (Add HW4 funcs to module2.py & attach flake8 res)
    rules = transcribtion_rules_DNA
    if "U" in seq or "u" in seq:
        rules = transcribtion_rules_RNA
    return "".join([rules[c] for c in seq])


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def reverse(seq: [str]):
    return seq[::-1]


def complement(seq: [str]):
=======
def reverse(seq:List[str]):
    return seq[::-1]


def complement(seq:List[str]):
>>>>>>> 8fa1609 (Add HW3 funcs to module1)
=======
def reverse(seq: list[str]):
    return seq[::-1]


def complement(seq: list[str]):
>>>>>>> 7606f0f (Add HW4 funcs to module2.py & attach flake8 res)
=======
def reverse(seq: [str]):
    return seq[::-1]


def complement(seq: [str]):
>>>>>>> ef83b33 (Update the main func and add flake8*.png)
    if 'U' in seq or 'u' in seq:
        rules = complimentary_rules_RNA
    else:
        rules = complimentary_rules_DNA
    result = str()
    for i in seq:
        if i in rules:
            result += rules[i]
    return result


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def reverse_complement(seq: [str]):
=======
def reverse_complement(seq:List[str]):
>>>>>>> 8fa1609 (Add HW3 funcs to module1)
=======
def reverse_complement(seq: list[str]):
>>>>>>> 7606f0f (Add HW4 funcs to module2.py & attach flake8 res)
=======
def reverse_complement(seq: [str]):
>>>>>>> ef83b33 (Update the main func and add flake8*.png)
    result = reverse(complement(seq))
    return result


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def gc_cont(seq: [str]):
    an_seq = seq.upper()
    g_count = an_seq.count("G")
    c_count = an_seq.count("C")
    result = ((g_count + c_count) / len(seq)) * 100
    return int(result)
=======
def gc_cont(seq:List[str]):
    seq_ = seq.upper()
    g_count = seq.count("G")
    c_count = seq.count("C")
    result = ((g_count + c_count) / len(seq)) * 100
    return int(result)
>>>>>>> 8fa1609 (Add HW3 funcs to module1)
=======
def gc_cont(seq: list[str]):
=======
def gc_cont(seq: [str]):
>>>>>>> ef83b33 (Update the main func and add flake8*.png)
    an_seq = seq.upper()
    g_count = an_seq.count("G")
    c_count = an_seq.count("C")
    result = ((g_count + c_count) / len(seq)) * 100
    return int(result)
>>>>>>> 7606f0f (Add HW4 funcs to module2.py & attach flake8 res)
