import unittest
def one_away(s1 : str,s2 : str )->bool:
    i=0

    if abs(len(s2)-len(s1))>1:
        return False

    length = min(len(s1), len(s2))

    while i<length:
        if s1[i] != s2[i]:
            break
        i+=1

    if len(s1) > len(s2):
        return s1[i+1:] == s2[i:]
    elif len(s2) > len(s1):
        return s2[i+1:] == s1[i:]
    else:
        return s1[i+1:] == s2[i+1:]

# class Test(unittest.TestCase):
#     '''Test Cases'''
#     data = [
#         ('pale', 'ple', True),
#         ('pales', 'pale', True),
#         ('pale', 'bale', True),
#         ('paleabc', 'pleabc', True),
#         ('pale', 'ble', False),
#         ('a', 'b', True),
#         ('', 'd', True),
#         ('d', 'de', True),
#         ('pale', 'pale', True),
#         ('pale', 'ple', True),
#         ('ple', 'pale', True),
#         ('pale', 'bale', True),
#         ('pale', 'bake', False),
#         ('pale', 'pse', False),
#         ('ples', 'pales', True),
#         ('pale', 'pas', False),
#         ('pas', 'pale', False),
#         ('pale', 'pkle', True),
#         ('pkle', 'pable', False),
#         ('pal', 'palks', False),
#         ('palks', 'pal', False)
#     ]
#
#     def test_one_away(self):
#         for [test_s1, test_s2, expected] in self.data:
#             actual = one_away(test_s1, test_s2)
#             self.assertEqual(actual, expected)
#
# if __name__ == "__main__":
#     unittest.main()