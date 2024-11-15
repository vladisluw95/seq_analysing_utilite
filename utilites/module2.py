<<<<<<< HEAD
from typing import Tuple, Union, List

=======
>>>>>>> 7606f0f (Add HW4 funcs to module2.py & attach flake8 res)
seqs = {
    # 'name' : ('sequence', 'quality')
    '@SRX079801': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079802': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'),
    '@SRX079803': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD'),
    '@SRX079804': ('TGAAGCGTCGATAGAAGTTAGCAAACCCGCGGAACTTCCGTACATCAGACACATTCCGGGGGGTGGGCCAATCCATGATGCCTTTG', 'FF@FFBEEEEFFEFFD@EDEFFB=DFEEFFFE8FFE8EEDBFDFEEBE+E<C<C@FFFFF;;338<??D:@=DD:8DDDD@EE?EB'),
    '@SRX079805': ('TAGGGTTGTATTTGCAGATCCATGGCATGCCAAAAAGAACATCGTCCCGTCCAATATCTGCAACATACCAGTTGGTTGGTA', '@;CBA=:@;@DBDCDEEE/EEEEEEF@>FBEEB=EFA>EEBD=DAEEEEB9)99>B99BC)@,@<9CDD=C,5;B::?@;A'),
    '@SRX079806': ('CTGCCGAGACTGTTCTCAGACATGGAAAGCTCGATTCGCATACACTCGCTGAGTAAGAGAGTCACACCAAATCACAGATT', 'E;FFFEGFGIGGFBG;C6D<@C7CDGFEFGFHDFEHHHBBHHFDFEFBAEEEEDE@A2=DA:??C3<BCA7@DCDEG*EB'),
    '@SRX079807': ('CATTATAGTAATACGGAAGATGACTTGCTGTTATCATTACAGCTCCATCGCATGAATAATTCTCTAATATAGTTGTCAT', 'HGHHHHGFHHHHFHHEHHHHFGEHFGFGGGHHEEGHHEEHBHHFGDDECEGGGEFGF<FGGIIGEBGDFFFGFFGGFGF'),
    '@SRX079808': ('GACGCCGTGGCTGCACTATTTGAGGCACCTGTCCTCGAAGGGAAGTTCATCTCGACGCGTGTCACTATGACATGAATG', 'GGGGGFFCFEEEFFDGFBGGGA5DG@5DDCBDDE=GFADDFF5BE49<<<BDD?CE<A<8:59;@C.C9CECBAC=DE'),
    '@SRX079809': ('GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT', 'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE'),
    '@SRX079810': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC', 'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE'),
    '@SRX079811': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA', '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'),
    '@SRX079812': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG', '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')
    }

<<<<<<< HEAD

def gc_bounds_12(*args: Tuple[float, float]) -> float:
    result = {}
    for key, (sequence, quality) in seqs.items():
        gc = sequence.count("G") + sequence.count("C")
        gc_cont = gc / len(sequence) * 100
        result[key] = gc_cont
    return result


def length_bounds_12(*args: Union[Tuple[int, int], List[int], int]) -> int:
    result = {}
    for key, (sequence, quality) in seqs.items():
        len_seq = len(sequence)
        result[key] = len_seq
    return result


def quality_threshold_12(int) -> str:
    result = {}
    for key, (sequence, quality) in seqs.items():
        q_score = (sum(ord(q)-33 for q in quality)/len(quality))
        result[key] = q_score
=======
phred = {
    '!': 0,
    '"': 1,
    '#': 2,
    '$': 3,
    '%': 4,
    '&': 5,
    "'": 6,
    '(': 7,
    ')': 8,
    '*': 9,
    '+': 10,
    ',': 11,
    '-': 12,
    '.': 13,
    '/': 14,
    '0': 15,
    '1': 16,
    '2': 17,
    '3': 18,
    '4': 19,
    '5': 20,
    '6': 21,
    '7': 22,
    '8': 23,
    '9': 24,
    ':': 25,
    ';': 26,
    '<': 27,
    '=': 28,
    '>': 29,
    '?': 30,
    '@': 31,
    'A': 32,
    'B': 33,
    'C': 34,
    'D': 35,
    'E': 36,
    'F': 37,
    'G': 38,
    'H': 39,
    'I': 40
}


def gc_bounds(gc_low: int, gc_high: int):
    result = {}
    for key, values in seqs.items():
        G_count = values[0].count("G")
        C_count = values[0].count("C")
        gc_content = ((G_count + C_count) / len(values[0])) * 100
        if gc_low <= gc_content <= gc_high:
            result[key] = values
    return result


def length_bounds(length_low: int, length_high: int):
    result = {}
    for key, values in seqs.items():
        len_seq = len(values[0])
        if len_seq >= length_low and len_seq <= length_high:
            result[key] = values
    return result


def quality_threshold(quality: int):
    result = {}
    for key, values in seqs.items():
        q_seq = 0
        for s in values[1]:
            if s in phred:
                q_seq += phred[s]
            else:
                q_seq += 0
        if quality <= q_seq:
            result[key] = values
>>>>>>> 7606f0f (Add HW4 funcs to module2.py & attach flake8 res)
    return result
