import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):
    jokes_list = []
    for i in range(num):
        _nouns = random.choice(nouns)
        _adverds = random.choice(adverbs)
        _adjectives = random.choice(adjectives)
        jokes_list.append(f'{_nouns } {_adverds} {_adjectives}')

    return jokes_list
print(get_jokes(2))






