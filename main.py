from functions_sources import read_txt
from functions_for_decrypt import analyse_seqs
from functions_for_decrypt import text_and_keys_analys

if __name__ == "__main__":
    txt = read_txt("Vigenere.txt")
    dell = analyse_seqs(txt,3, 5)
    g = text_and_keys_analys(txt, dell[0])
    print(g)