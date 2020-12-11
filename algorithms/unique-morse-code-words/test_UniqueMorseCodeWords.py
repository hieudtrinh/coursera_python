from unittest import TestCase

from UniqueMorseCodeWords import UniqueMorseCodeWords


class TestUniqueMorseCodeWords(TestCase):
    def test_unique_morse_representations(self):
        self.solution = UniqueMorseCodeWords()
        words = ["gin", "zen", "gig", "msg"]
        self.assertEqual(self.solution.uniqueMorseRepresentations(words), 2)
        self.assertEqual(self.solution.uniqueMorseRepresentations2(words), 2)
