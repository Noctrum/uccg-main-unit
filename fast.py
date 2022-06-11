from collections import Counter
sequence = "AGAGKTAGAT" * 1000000


def count_string(seq):
    return [seq.count("A"), seq.count('G'), seq.count('T'), seq.count('K')]

count_string(sequence)
