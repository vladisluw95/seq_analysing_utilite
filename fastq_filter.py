from Bio import SeqIO  # with SeqIo we can work fast* format files
from Bio.SeqUtils import gc_fraction  # SeqUtils contains list function for working with fast* files, for example gc_fraction 
import argparse
import logging
import sys

logging.basicConfig(
    style="{",
    format="{levelname}: {asctime}  {message}",
    level=logging.INFO,
    filename="app.log",
    filemode="a",
    force=True
)


def filter_fastq(input_file: str, output_file: str,
                 min_len: float = 0, max_len: float = float('inf'),
                 min_quality: float = 0,
                 min_gc: float = 0, max_gc: float = 100):
    logging.info(
        f"Start filtering with following params: "
        f"len=[{min_len}-{max_len}], quality>={min_quality}, "
        f"GC%=[{min_gc}-{max_gc}]"
    )
    try:
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
                        logging.info(f"filter_fastq: {output_fastq}")
    except Exception as e:
        logging.error(f"Error: {e}", exc_info=True)
        raise


def parse_args():
    parser = argparse.ArgumentParser(prog='fastq filter',
                    description='This tool filtrates fastq files',
                    epilog='Examples: ' \
                    'filter_fastq(input_file, output_fastq, -mn 0, -mx 1000, -q 0, -mngc 40, -maxgc 60)')

    parser.add_argument('positional', type=str, help='input file [fastq format only] (required)')
    parser.add_argument('-o', '--ouput-file', type=str, help='output file [fastq reccomended] (required)')
    parser.add_argument('-mn', '--min-len', type=float, help='minimum length [float] (default = 0.0)')
    parser.add_argument('-mx', '--max-len', type=float, help='maximum length [float] (required)')
    parser.add_argument('-q', '--min-quality', type=float, help='minimum quality [float] (default = 0.0)')
    parser.add_argument('-mngc', '--min-gc', type=float, help='minimum gc-content [float] (default = 0.0)')
    parser.add_argument('-mxgc', '--max-gc', type=float, help='maximum gc-content [float] (default = 100.0)')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    filter_fastq(
        input_file=args.input_file,
        output_file=args.output_file,
        min_len=args.min_len,
        max_len=args.max_len,
        min_quality=args.min_quality,
        min_gc=args.min_gc,
        max_gc=args.max_gc
    )
