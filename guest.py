from invite import Invite
from review import Review

class Guest:

    _all = []

    def __init__(self, name):
        self._name = name
        Guest._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

#    @property
    def reviews(self):
        return [review for review in Review.all() if review.reviewer == self]

#    @property
    def invites(self):
        return [invite for invite in Invite.all() if invite.guest == self]

#    @property
    def number_of_invites(self):
        return len(self.invites())

    @classmethod
    def all(cls):
        return cls._all

    def rsvp(self, invite, rsvp_status):
        for card in self.invites():
            if card == invite:
                card.accepted = rsvp_status
                return card.accepted #rsvp_status

    def review_recipe(self, recipe, rating, comment):
        Review(self, recipe, rating, comment)
        return [review for review in Review.all() if review.recipe == recipe]

    def favorite_recipe(self):
        top_rating = 0
        top_recipe = None
        for review in self.reviews():
            if review.rating > top_rating:
                top_rating = review.rating
                top_recipe = review.recipe
        return top_recipe

    @classmethod
    def most_popular(cls):
        most_invites = 0
        most_invited_guest = None
        for person in cls.all():
            if person.number_of_invites() > most_invites:
                most_invites = person.number_of_invites()
                most_invited_guest = person
        return most_invited_guest

    def avg_rating(self):
        my_ratings = [review.rating for review in self.reviews()]
        return (sum(my_ratings)/len(my_ratings))

    @classmethod
    def toughest_critic(cls):
        tough_critic = None
        tough_avg_rating = 10
        for guest in cls.all():
            if guest.avg_rating() < tough_avg_rating:
                tough_avg_rating = guest.avg_rating()
                tough_critic = guest
        return tough_critic

    @classmethod
    def most_active_critic(cls):
        most_reviews = 0
        most_critical = None
        for critic in cls.all():
            if len(critic.reviews()) > most_reviews:
                most_reviews = len(critic.reviews())
                most_critical = critic
        return most_critical
