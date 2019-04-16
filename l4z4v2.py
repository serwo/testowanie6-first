from functools import reduce

"""
Program do podziału tekstu na słowa oraz tworzenia statystyki długości słów.
"""

# === Podział tekstu na słowa ===


class split_text(object):
    """
    Przetwarzanie tekstu rozpoczyna się od połączenia słów przenoszonych do
    nowej linii. Następnie usuwane są znaki interpunkcyjne. Kolejnym krokiem
    jest zamiana tekstu na listę słów oraz usunięcie z niej znaków '-'.
    """
    def __init__(self, text):
        self.text = reduce((
            lambda acc, x: (
                acc + x.rstrip('-') if x.endswith('-') else acc + x + ' ')),
                text.split('\n'), "")
        sign_list = ['.', ',', ';', '!', '?', '/', '\\',
                     '(', ')', '[', ']', '{', '}']
        self.text = "".join(map(
            (lambda x: ' ' if x in sign_list else x), self.text)).split()
        if '-' in self.text:
            self.text.remove('-')
        self.word_position = -1
        self.len = len(self.text)

    def __iter__(self):
        return self

    def __str__(self):
        return self.word

    def __next__(self):
        self.word_position += 1
        if self.word_position > self.len - 1:
            raise StopIteration
        else:
            return self.text[self.word_position]


# === Tworzenie statystyki długości słów ===


class statistics(object):
    """
    Tworzony jest słownik, w którym kluczem jest długość słowa, a wartością
    lista słów.
    """
    def __init__(self, words_list):
        self.dict = {}
        for word in words_list:
            word_len = len(word)
            if word_len in self.dict:
                if word not in self.dict[word_len]:
                    self.dict[word_len].append(word)
            else:
                self.dict[word_len] = [word]

    def get_stats_as_dict(self):
        return self.dict

    def print_statistics(self):
        stats = self.get_stats_as_dict()
        for key, value in stats:
            print(key, ': ', ', '.join(value))


with open('krywulki.txt', 'r') as t:
    text = t.read()
    words = split_text(text)
    for word in words:
        print(word)
    lengths_dict = statistics(words)
    lengths_dict.print_statistics()
