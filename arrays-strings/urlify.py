import unittest
def urlify(s:str, length:int)->list:
    space_count = 0
    for i in range(length):
        if s[i] == " ":
            space_count += 1
    new_str_len = (length + space_count * 3) - space_count

    ind = 0
    new_str = [""]*new_str_len
    replace = "%20"

    for i in range(length):
        if s[i] == " ":
            #insert the replace sequence in place of the " "
            for j in range(len(replace)):
                new_str[ind+j] = replace[j]
            #increment ind to next position that is to be inserted
            ind += len(replace)
        else:
            #copy from original string if not " "
            new_str[ind] = s[i]
            ind += 1

        if ind == new_str_len:
            break

    return new_str

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()