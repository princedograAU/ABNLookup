import unittest
from abn_lookup import ABNService


class TestABNLookup(unittest.TestCase):

    def test_search_by_abn(self):
        sample_abn = '50110219460'
        response = ABNService.search_by_abn_post(abn=sample_abn)
        self.assertNotIn('exception', response)

    def test_search_by_name(self):
        sample_name = 'avengers'
        response = ABNService.search_by_name_post(name=sample_name)
        self.assertNotIn('exception', response)

    def test_search_by_acn(self):
        sample_acn = '110219460'
        response = ABNService.search_by_acn_post(acn=sample_acn)
        self.assertNotIn('exception', response)


if __name__ == '__main__':
    unittest.main()
