import unittest
def check_permutation(str1 : str, str2 : str) -> bool:
    string_dict = {}
    for char in str1:
        if char not in string_dict:
            string_dict[char]=1
        else:
            string_dict[char] = 1

    for char in str2:
        if char not in string_dict:
            return False
        else:
            string_dict[char]-=1

    for char in string_dict:
        if string_dict[char]>0:
            return False

    return True

# class Test(unittest.TestCase):
#     dataT = (
#         ('abcd', 'bacd'),
#         ('3563476', '7334566'),
#         ('wef34f', 'wffe34'),
#     )
#     dataF = (
#         ('abcd', 'd2cba'),
#         ('2354', '1234'),
#         ('dcw4f', 'dcw5f'),
#     )
#
#     def test_cp(self):
#         # true check
#         for test_strings in self.dataT:
#             result = check_permutation(*test_strings)
#             self.assertTrue(result)
#         # false check
#         for test_strings in self.dataF:
#             result = check_permutation(*test_strings)
#             self.assertFalse(result)
#
#
# if __name__ == "__main__":
#     unittest.main()




