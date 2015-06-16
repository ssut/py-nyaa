import unittest
from nyaa import nyaa

class NyaaTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic(self):
        results = [
            nyaa.search()[0],
            nyaa.search('horrible subs', 2, '-seeders')[0],
            nyaa.search('horrible subs', 1, 'seeders')[0],
        ]

        assert results[0].title != ''
        assert results[1].seeders > 0
        assert results[2].seeders == 0

if __name__ == '__main__':
    unittest.main()
