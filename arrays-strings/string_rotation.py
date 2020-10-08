#@author : Gaurav Pai
#data-created : 10/08/20

import unittest
def is_substring(string : str, sub : str) -> bool:
    return string.find(sub) != -1

def string_rotation(s1 : str, s2 : str)->bool:
    if len(s1)!=len(s2):
        return False
    return is_substring(s1+s1, s2)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
