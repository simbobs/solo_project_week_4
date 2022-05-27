class City:
    def __init__(self, name, country, visited = False, id = None):
        self.name = name
        self.country = country
        # self.comments = comments
        self.visited = visited
        self.id = id
        
    def mark_city_visited(self):
        self.visited = True
