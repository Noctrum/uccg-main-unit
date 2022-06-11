from collections import Counter
sequence = "AGAGKTAGAT" * 1000000 


def count_Counter(seq):
    counter = Counter(seq)
    return [counter["A"], counter["G"], counter["T"], counter["K"]]

count_Counter(sequence)