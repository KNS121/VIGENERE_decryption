import re

def read_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        full_text = file.read()
        full_text = full_text.lower()
    full_text = re.sub('[^а-яё]', '', full_text)
    return full_text

#print(read_txt("Vigenere.txt"))

alphavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def freq_language_analys_get(filename):

    frequencies = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                char, freq = line.split()
                frequencies[char] = float(freq)

    return frequencies