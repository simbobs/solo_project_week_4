import unittest
from models.sight import Sight

class TestSight(unittest.TestCase):
    
    def setUp(self):
        self.sight = Sight("Edinburgh Castle", "Very impressive castle, would visit again", "Edinburgh", id= None)

    def test_sight_has_name(self):
        self.assertEqual("Edinburgh Castle", self.sight.name)
        
    def test_sight_has_comment(self):
        self.assertEqual("Very impressive castle, would visit again", self.sight.comment)
    
    def test_sight_has_city(self):
        self.assertEqual("Edinburgh", self.sight.city)
    
    def test_sight_has_none_id(self):
        self.assertIsNone(self.sight.id)