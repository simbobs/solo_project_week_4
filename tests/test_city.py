import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city1= City("Glasgow", "Scotland", visited = False, id = None)
    
    def test_city_has_name(self):
        self.assertEqual("Glasgow", self.city1.name)
    
    def test_city_has_country(self):
        self.assertEqual("Scotland", self.city1.country)
        
    # def test_city_has_comments(self):
    #     self.assertEqual("Rubbish weather but people are nice", self.city1.comments)
    
    def test_city_has_not_been_visited(self):
        self.assertEqual(False, self.city1.visited)
    
    def test_city_has_none_id(self):
        self.assertIsNone(self.city1.id)
    
    def test_city_has_been_visited(self):
        self.city1.mark_city_visited()
        self.assertTrue(self.city1.visited)
    
    

