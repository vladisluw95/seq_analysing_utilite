import pytest
from fastq_filter import filter_fastq


@pytest.mark.parametrize(
    "input_file,output_file, min_len,max_len,min_quality,min_gc,max_gc, result",
    [
            ('input.fastq', 'output.fastq', 0, 100, 0, 0, 100, True),
            ('input.fastq', 'output.fastq', 0, 100, 0, 100, 10, False)
    ]
)
def test_output(input_file, output_file, min_len, max_len, min_quality,
                min_gc, max_gc, result):
    assert filter_fastq(input_file, output_file, min_len, max_len, min_quality,
                        min_gc, max_gc) == result
