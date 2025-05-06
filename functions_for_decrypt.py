from math import gcd

def analyse_seqs(txt, min_seq_len):

    #search repeat seqs
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



    # search NOD
    deliteli_array = []

    for i in range(len(distances_between_repeats_array)):
        for j in range(i + 1, len(distances_between_repeats_array)):

            NOD = gcd(distances_between_repeats_array[i],
                      distances_between_repeats_array[j])

            deliteli_array.append(NOD)

    # the most popular delitels
    freq_array = {}
    for d in deliteli_array:
        freq_array[d] = freq_array.get(d, 0) + 1

    return freq_array



