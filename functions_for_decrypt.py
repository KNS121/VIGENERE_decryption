import math
from math import gcd
from functions_sources import alfavit, read_txt, freq_language_analys_get, clean_txt


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

    unique_lens = []
    for length in sorted(lenghs_of_key):
        if not any(length % l == 0 and l != length for l in unique_lens):
            unique_lens.append(length)

    return unique_lens[:kolvo_top_del]

def get_groups_by_key_lengths(text, key_length):

    groups = [''] * key_length
    for i, char in enumerate(text):
        groups[i % key_length] += char

    return groups


def search_sdvig(alfavit, freqs_in_language, group):
    sdvig = 0
    literal_freq = -math.inf
    len_alfavit = len(alfavit)

    for current_sdvig in range(len_alfavit):
        current_literal_freq = 0
        for literal in group:
            #reverse Vigenere
            original_index = (alfavit.index(literal) - current_sdvig) % len_alfavit
            original_char = alfavit[original_index]
            current_literal_freq += freqs_in_language.get(original_char, 0)

        if current_literal_freq > literal_freq:
            literal_freq = current_literal_freq
            sdvig = current_sdvig
    return sdvig


def decrypt_text(original_text, key, alfavit):

    decrypted = []
    key_indices = [alfavit.index(k) for k in key]
    key_len = len(key)
    key_pos = 0

    for literal in original_text:
        if literal.lower() in alfavit:
            decrypt_idx = alfavit.index(literal.lower())
            original_idx = (decrypt_idx - key_indices[key_pos % key_len]) % len(alfavit)
            decrypted_char = alfavit[original_idx]
            decrypted.append(decrypted_char.upper() if literal.isupper() else decrypted_char)
            key_pos += 1

        else:
            decrypted.append(literal)

    return ''.join(decrypted)


def calculate_err(decrypted_text, reference_freq):
    text = clean_txt(decrypted_text)
    total = max(len(text), 1)
    current_freq = {char: text.count(char) / total for char in alfavit}

    err = 0
    for char in alfavit:
        err += (current_freq.get(char, 0) - reference_freq.get(char, 0)) ** 2
    return 1 / (1 + err)



def calculate_accuracy(text, freqs):
    clean = clean_txt(text)
    total = len(clean) or 1
    text_freq = {char: clean.count(char) / total for char in alfavit}
    return sum(min(freq, text_freq[char]) for char, freq in freqs.items())


def main_decrypt():
    original_text = read_txt("Vigenere.txt")
    clean_text = clean_txt(original_text)
    freqs = freq_language_analys_get("freqs.txt")

    key_lengths = analyse_seqs(clean_text, min_seq_len=3, kolvo_top_del=5)
    print(f"Searched len of key: {key_lengths}")

    best_key = None
    best_score = 0

    for length in key_lengths:

        groups = get_groups_by_key_lengths(clean_text, length)
        key = [alfavit[search_sdvig(alfavit, freqs, group)] for group in groups]
        decrypted = decrypt_text(original_text, key, alfavit)

        err = calculate_accuracy(decrypted, freqs)
        print(f"len {length}: key '{''.join(key)}' - error of freq {err:.5%}")

        if err > best_score:
            best_score = err
            best_key = key

    # Save decrypted text
    if best_key:
        result = decrypt_text(original_text, best_key, alfavit)
        with open("decrypted_text.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print(f"\nthe best key: {''.join(best_key)}")
        print(f"error of freq: {best_score:.2%}")
        print("decrypted text was saved in decrypted_text.txt")
    else:
        print("Can't search key :((((")









