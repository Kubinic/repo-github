rus_eng = {
    'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
    'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
}

def num_translate(eng_word):
    return rus_eng.get(eng_word)
print(num_translate('two'))