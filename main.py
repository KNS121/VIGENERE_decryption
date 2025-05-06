from functions_sources import read_txt
from functions_for_decrypt import analyse_seqs

if __name__ == "__main__":
    txt = read_txt("Vigenere.txt")
    dell = analyse_seqs(txt,3, 5)

    print(dell)