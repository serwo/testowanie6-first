import unittest
from l4z4v2 import split_text, statistics


class TestSplitText(unittest.TestCase):
    def test_empty_text_returns_no_words(self):
        text = ''
        result = list(split_text(text))
        print(result)
        self.assertEqual(result, [])

    def test_only_signs_returns_no_words(self):
        text = '''?? . ? / \\ - ([]) { } \n !'''
        result = list(split_text(text))
        print(result)
        self.assertEqual(result, [])

    def test_text_without_dashes_success(self):
        text = '''word1 word2 word3
        word4 word5 word6'''
        result = list(split_text(text))
        print(result)
        self.assertEqual(result, 
            ['word1', 'word2', 'word3', 'word4', 'word5', 'word6'])

    def test_dash_at_the_end_of_line_joins_word(self):
        text = '''Ewa idzie spać. Musi jesz-\ncze
         wziąc prysznic.'''
        result = list(split_text(text))
        print(result)
        self.assertEqual(result, ['Ewa', 'idzie', 'spać', 'Musi',
            'jeszcze', 'wziąc', 'prysznic'])

    def test_dash_inside_word_doesnt_split_word(self):
        text = '''Flaga Polski - biało-czerwona.'''
        result = list(split_text(text))
        print(result)
        self.assertEqual(result, ['Flaga', 'Polski', 'biało-czerwona'])


class TestPrintStatistics(unittest.TestCase):
    def test_empty_list_empty_dict(self):
        words = []
        stats = statistics(words)
        result = stats.get_stats_as_dict()
        
        self.assertEqual(result, {})

    def test_repetiting_words_only_once(self):
        words = ['kot', 'jabłko', 'rower', 'kot', 'kot']
        stats = statistics(words)
        result = stats.get_stats_as_dict()

        self.assertEqual(result, {3: ['kot'], 5: ['rower'], 6: ['jabłko']})

    
