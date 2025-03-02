from Bio import SeqIO  # with SeqIo we can work fast* format files
from Bio.SeqUtils import gc_fraction  # SeqUtils contains list function for working with fast* files, for example gc_fraction 


def filter_fastq(input_file: str, output_file: str,
                 min_len: float = 0, max_len: float = float('inf'),
                 min_quality: float = 0,
                 min_gc: float = 0, max_gc: float = 100):
    with open(input_file, 'r') as input_fastq, open(output_file, 'w') as output_fastq:
        for record in SeqIO.parse(input_fastq, 'fastq'): # SeqIO.parse reads records in file.fastq
            rec_len = len(record.seq) # .seq is object of Seq class, sequnce of nucleotides
            rec_qual = sum(record.letter_annotations['phred_quality'])/rec_len  # .letter_annotations is an atribute of SeqRecord object
            # .letter_annotations is a dict, with phred_quality' keys
            rec_gc = gc_fraction(record.seq)*100  # gc_fraction is method for calculating of gc contain
            if (min_len <= rec_len <= max_len and
                min_quality <= rec_qual and
                min_gc <= rec_gc <= max_gc):
                SeqIO.write(record, output_fastq, 'fastq')


input_file = 'input_fastq.fastq'
output_fastq = 'filtered.fastq'

filter_fastq(input_file, output_fastq, min_len=0, max_len=1000, min_quality=0, min_gc=40, max_gc=60)



