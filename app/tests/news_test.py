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

import unittest
from ..models import Sources

class SourceTest(unittest.TestCase):
    def setUp(self):
        self.source = Sources(
            "ABC News", 
            "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", 
            "https://abcnews.go.com/"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.source, Sources))

if __name__ == "__main__":
    unittest.main()