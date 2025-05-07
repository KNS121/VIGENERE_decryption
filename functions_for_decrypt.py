import math
from math import gcd

def analyse_seqs(txt, min_seq_len, kolvo_top_del):

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



    # the most popular delitels = vozmozghnaya dlina klucha
    freq_array = {}
    for d in deliteli_array:
        freq_array[d] = freq_array.get(d, 0) + 1

    sort_freq = sorted(freq_array.items(), key=lambda x: (-x[1], -x[0]))

    top_delitels = []

    for i in sort_freq[:kolvo_top_del]:
        if i[0] > 1:
            top_delitels.append(i[0])

    lenghs_of_key = top_delitels

    return lenghs_of_key

def get_groups_by_key_lengths(text, key_length):

    groups = [''] * key_length
    for i, char in enumerate(text):
        groups[i % key_length] += char
    print('__________________________')
    print(groups)

    return groups

# def search_sdvig(alfavit, freqs_in_language, groups):
#     err = math.inf
#     alfavit_len = len(alfavit)
#
#     for sdvig in range(alfavit_len):
#         err_fact =








