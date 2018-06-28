import unittest
from .models import news

News = news.News


class NewsTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_news = News(1234, 'Amazing news', 'Thrilling news', 'https://abcnews.go.com', 'Technology',
                             'UnitedStates', 'English')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


if __name__ == '__main__':
    unittest.main()
