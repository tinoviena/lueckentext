import source.articles
import unittest


class TestArticles(unittest.TestCase):
    result = source.articles.all()
    print(f"alle artikel: {result}")
    def test_all(self):
        self.assertFalse(self.result==None, "List of articles should not be None")
        self.assertIn("die", self.result)
        self.assertNotIn("fall", self.result)
        self.assertNotIn("akkusativ", self.result)

if __name__ == '__main__':
    unittest.main()