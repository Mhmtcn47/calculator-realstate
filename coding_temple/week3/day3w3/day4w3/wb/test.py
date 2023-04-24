import unittest

from wb import create_string_hash_map_handle_contractions as create_string_hash_map

class Test_Create_String_Hash_Map(unittest.TestCase):

    def test_simple_string(self):
        result = create_string_hash_map('to be or not to be')
        expected_output = {'to': 2, 'be': 2, 'or': 1, 'not': 1}
        self.assertEqual(result,expected_output)
        self.assertNotEqual(result, {'to':1})

    def test_contractions(self):
        result = create_string_hash_map("to't be't or'1 not to be")
        expected_output = {'t':2, 'I':1, 'to':2, 'be':2, 'or':1, 'not':1}
        self.assertEqual(result, expected_output)

    def test_casing(self):
        self.assertEqual(create_string_hash_map('To to be be'), {'to':2, 'be':2})


    def test_punctuation(self):
        result = create_string_hash_map('to be or not to be!!')
        expected_output = ('to':2, 'be':2, 'or':1, 'not':1)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()