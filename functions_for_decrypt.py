def find_seq_repeats(txt, min_seq_len):
    seq_dict = {}

    for i in range(len(txt)-min_seq_len + 1):
        seq = txt[i:i+min_seq_len]

        if seq not in seq_dict:
            seq_dict[seq] = []

        seq_dict[seq].append(i)

    result_dict = {}

    for seq, positions in seq_dict.items():
        if len(positions) > 1:
            result_dict[seq] = positions

    return result_dict