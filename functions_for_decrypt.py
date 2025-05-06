def analyse_seqs(txt, min_seq_len):
    seq_dict = {}

    for i in range(len(txt)-min_seq_len + 1):
        seq = txt[i:i+min_seq_len]

        if seq not in seq_dict:
            seq_dict[seq] = []

        seq_dict[seq].append(i)

    result_dict_seq = {}

    for seq, positions in seq_dict.items():
        if len(positions) > 1:
            result_dict_seq[seq] = positions


    #dist between repeats
    distances_between_repeats_array = []

    for pos in seq_dict.values():
        if len(pos) > 1:
            for i in range(1, len(pos)):
                distances_between_repeats_array.append(pos[i] - pos[0])

    return distances_between_repeats_array