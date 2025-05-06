from functions_sources import read_txt
from functions_for_decrypt import find_seq_repeats

if __name__ == "__main__":
    txt = read_txt("Vigenere.txt")
    res_dict = find_seq_repeats(txt,3)

    print(res_dict)