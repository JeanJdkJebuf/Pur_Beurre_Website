from django.test import TestCase

from ..related_functions import symbol_removal

class functionsTestCase(TestCase):

    def test_symbol_removal_working(self):
        """Test that symbol removal works"""
        entry = "jéâî"
        answer = symbol_removal(entry)
        self.assertEqual("jeai", answer)
