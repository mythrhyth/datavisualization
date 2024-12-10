import unittest
import requests

class TestPythonRepos(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        cls.response = requests.get(url)
        cls.response_data = cls.response.json()
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200, 'Status code is not 200')
        
    def test_items_returned(self):
        items = self.response_data.get('items', [])
        self.assertEqual(len(items), 30, 'Number of items returned is not 30.')
        
    def test_total_repositories(self):
        total_repositories = self.response_data.get('total_count', 0)
        self.assertGreater(total_repositories, 100000, 'Total repositories are not greater than 1,00,000')
    def test_item_keys(self):
        items = self.response_data.get('items', [])
        if items:
            for item in items:
                self.assertIn('name', item, 'Repository item missing "name"')
                self.assertIn('owner', item, 'Repository item missing "owner"')
                self.assertIn('html_url', item, 'Repository item missing "html_url"')
        else:
            self.fail('NO items found in the API response.')
            
if __name__ == '__main__':
    unittest.main()