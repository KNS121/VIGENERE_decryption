from collections import defaultdict, Counter

def find_repeated_sequences(text, min_length=2):

    sequences = defaultdict(list)

    for i in range(len(text) - min_length + 1):

        seq = text[i:i+min_length]
        sequences[seq].append(i)

    return {seq: pos for seq, pos in sequences.items() if len(pos) > 1}