


def palindrome_permutation(s : str)->bool:
    # my approach
    # char_dict = {}
    # odd_count = 0
    # for char in s:
    #     if char not in char_dict:
    #         char_dict[char]=1
    #     else:
    #         char_dict[char]+=1
    #
    #     if char_dict[char] % 2 != 0:
    #         odd_count += 1
    #     else:
    #         odd_count -= 1
    #
    # print(odd_count<=1)

    # elegant approach
    # whenever there is a problem of checking evens and odds,
    # try using bit vector as even toggles leaves it at original state,
    # odd toggles leaves it at opposite state
    char_dict = {}
    for char in s.lower():
        if char ==" ":
            continue
        if char not in char_dict:
            char_dict[char] = 1
        else:
            if char_dict[char] == 0:
                char_dict[char] = 1
            else:
                char_dict[char] = 0
    return (sum(char_dict.values())<=1)




# import unittest
# class Test(unittest.TestCase):
#     '''Test Cases'''
#     data = [
#         ('Tact Coa', True),
#         ('jhsabckuj ahjsbckj', True),
#         ('Able was I ere I saw Elba', True),
#         ('So patient a nurse to nurse a patient so', False),
#         ('Random Words', False),
#         ('Not a Palindrome', False),
#         ('no x in nixon', True),
#         ('azAZ', True)]
#
#     def test_pal_perm(self):
#         for [test_string, expected] in self.data:
#             actual = palindrome_permutation(test_string)
#             self.assertEqual(actual, expected)
#
# if __name__ == "__main__":
#     unittest.main()