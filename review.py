class Review:

    _all = []

    def __init__(self, reviewer, recipe, rating, comment):
        self._reviewer = reviewer
        self._recipe = recipe
        self._rating = rating
        self._comment = comment
        Review._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def recipe(self):
        return self._recipe

    @property
    def rating(self):
        return self._rating

    @property
    def comment(self):
        return self._comment

    @property
    def reviewer(self):
        return self._reviewer
