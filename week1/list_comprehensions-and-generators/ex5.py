text_as_string = ("The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains "
                  "all of the letters of the English alphabet")

def calculate_letters(str):
    split_text = str.split()
    calculated_letters = [len(word) for idx, word in enumerate(split_text) if idx != 0]
    return calculated_letters

print(calculate_letters(text_as_string))
