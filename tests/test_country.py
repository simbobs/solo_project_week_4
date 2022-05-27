import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country1 = Country("Scotland", visited = False, id = None)
        
    def test_country_has_name(self):
        self.assertEqual("Scotland",self.country1.name)
    
    def test_country_has_not_been_visited(self):
        self.assertFalse(self.country1.visited)
        
    def test_country_has_none_id(self):
        self.assertIsNone(self.country1.id)
    
    
    def test_country_has_been_visited(self):
        self.country1.mark_country_visited()
        self.assertEqual(True, self.country1.visited)
        