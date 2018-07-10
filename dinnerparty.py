from invite import Invite
from course import Course
from review import Review

class DinnerParty:

    _all = []

    def __init__(self, party):
        self._party = party
        DinnerParty._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def party(self):
        return self._party

#    @property
    def invites(self):
        return [invite for invite in Invite.all() if invite.dinner_party == self]

#    @property
    def guests(self):
        return [invite.guest for invite in Invite.all() if invite.dinner_party == self]

#    @property
    def number_of_attendees(self):
        coming = []
        for invite in self.invites():
            if invite.accepted == True:
                coming.append(invite)
        return len(coming)

    def courses(self):
        return [course for course in Course._all if course.dinner_party == self]

    def recipes(self):
        return [course.recipe for course in Course._all if course.dinner_party == self]

    def recipe_count(self):
        return len(self.recipes())

    def reviews(self):
        recipe_names = [recipe.name for recipe in self.recipes()]
        return [review for review in Review.all() if review.recipe.name in recipe_names]

    def highest_rated_recipe(self):
        rating = 0
        top_recipe = None
        for review in self.reviews():
            if review.rating > rating:
                rating = review.rating
                top_recipe = review.recipe
        return top_recipe
