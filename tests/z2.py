from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class TestWikidepia(unittest.TestCase):
    bs = None

    def setUp(self) -> None:
        url = 'https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%81%D0%BA,_%D0%98%D0%BB%D0%BE%D0%BD'
        TestWikidepia.bs = BeautifulSoup(urlopen(url), 'lxml')

    def test_1(self):
        pageTitle = TestWikidepia.bs.find("h1").get_text()
        self.assertEqual('Маск, Илон', pageTitle)

    def test_2(self):
        spanTitle = TestWikidepia.bs.find("span", {'class': 'infobox-above'})
        if spanTitle is not None:
            self.assertEqual('Илон Маск', spanTitle)
        else:
            return False



if __name__ == '__main__':
    unittest.main()