import source.replace
import unittest


class TestReplaceArticles(unittest.TestCase):
    test_string = "Das ist ein einfacher Test."
    (result, replacements) = source.replace.replace(test_string)
    
    print(f"neuer text: {result}")
    def test_replace_text(self):
        self.assertFalse(self.result==None, "Only articles should be removed")
        pieces = self.result.split()
        self.assertEqual(len(pieces), len(self.test_string.split()))
        self.assertEqual(self.result, "__ ist ein einfacher Test.")

    def test_replace_replacements(self):
        self.assertFalse(self.replacements==None, "Something should have been replaced")
        self.assertEqual([("Das", 0)], self.replacements)


    test_string2 = "Ein Test ist der Test."
    (result2, replacements2) = source.replace.replace(test_string2)

    def test_replace_replacements2(self):
        print(f"2222222222222222222222222222222222result2 {self.result2}")
        self.assertFalse(self.replacements2==None, "Something should have been replaced")
        self.assertEqual([("der", 13)], self.replacements2)
        print(f"{self.test_string2[self.replacements2[0][1]:self.replacements2[0][1]+3]}")


if __name__ == '__main__':
    unittest.main()