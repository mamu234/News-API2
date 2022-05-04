import unittest
from ..models import Articles


class NewsTest(unittest.TestCase):
    def setUp(self):
        self.articles = Articles(
          "cnn.com", 
            "Stephen Collinson", 
            "Supreme Court's draft opinion sends electric shock through midterm campaigns" 
            "https://us.cnn.com/2022/05/04/politics/supreme-court-draft-opinion-midterm-shock/index.html"
            
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.articles, Articles))

if __name__ == "__main__":
    unittest.main()