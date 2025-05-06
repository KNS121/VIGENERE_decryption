import re

def read_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        full_text = file.read()
        full_text = full_text.lower()
    full_text = re.sub('[^а-яё]', '', full_text)
    return full_text

print(read_txt("Vigenere.txt"))
