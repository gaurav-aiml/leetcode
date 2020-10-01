import unittest


def string_compression(s: str) -> str:
    i = 0
    j = 1
    new_str = []
    while i < len(s) and j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            new_str.append(s[i])
            new_str.append(str(j - i))
            i = j
            j += 1


    new_str.append(s[i])
    new_str.append(str(j - i))


    # do not use string concatenation while building a string
    #always use .join(list) while building string

    return min(s, "".join(new_str), key=len)

# class Test(unittest.TestCase):
#     '''Test Cases'''
#     data = [
#         ('aabcccccaaa', 'a2b1c5a3'),
#         ('abcdef', 'abcdef')
#     ]
#
#     def test_string_compression(self):
#         for [test_string, expected] in self.data:
#             actual = string_compression(test_string)
#             self.assertEqual(actual, expected)
#
# if __name__ == "__main__":
#     unittest.main()