from review import Review

class Recipe:

    _all = []

    def __init__(self, name):
        self._name = name
        Recipe._all.append(self)

    @property
    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls._all

    def reviews(self):
        return [review for review in Review.all() if review.recipe == self]

    def avg_rating(self):
        recipe_ratings = [review.rating for review in self.reviews()]
        if len(recipe_ratings) > 0:
            return (sum(recipe_ratings)/len(recipe_ratings))
        else:
            return None

    @classmethod
    def top_three(cls):

        recipe_dict = {recipe : recipe.avg_rating() for recipe in cls.all() if recipe.avg_rating() != None}
        sorted_list = sorted(recipe_dict, key = recipe_dict.get, reverse = True)
        return sorted_list[0:3]

    @classmethod
    def bottom_three(cls):
        recipe_dict = {recipe : recipe.avg_rating() for recipe in cls.all() if recipe.avg_rating() != None}
        sorted_list = sorted(recipe_dict, key = recipe_dict.get)
        return sorted_list[0:3]

    def top_five_reviews(self):
        return sorted(self.reviews(), key = lambda x: x.rating) [0:5]
