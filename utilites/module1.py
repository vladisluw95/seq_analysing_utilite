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


def transcribe(seq: list[str]):
    rules = transcribtion_rules_DNA
    if "U" in seq or "u" in seq:
        rules = transcribtion_rules_RNA
    return "".join([rules[c] for c in seq])


def reverse(seq: list[str]):
    return seq[::-1]


def complement(seq: list[str]):
    if 'U' in seq or 'u' in seq:
        rules = complimentary_rules_RNA
    else:
        rules = complimentary_rules_DNA
    result = str()
    for i in seq:
        if i in rules:
            result += rules[i]
    return result


def reverse_complement(seq: list[str]):
    result = reverse(complement(seq))
    return result


def gc_cont(seq: list[str]):
    an_seq = seq.upper()
    g_count = an_seq.count("G")
    c_count = an_seq.count("C")
    result = ((g_count + c_count) / len(seq)) * 100
    return int(result)
