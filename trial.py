from review import Review
from invite import Invite
from dinnerparty import DinnerParty
from recipe import Recipe
from guest import Guest
from course import Course

#Create guests
stacy = Guest('Stacy')
bob = Guest('Bob')

#Create Parties
party1 = DinnerParty('party1')

#Create Invites
invite1 = Invite(party1, stacy)
invite2 = Invite('party2', stacy)
invite3 = Invite('party3', bob)

#Create Recipes
recipe1 = Recipe('Borscht')
recipe2 = Recipe('Burgers')
recipe3 = Recipe('Sushi')
recipe4 = Recipe('Pizza')
recipe5 = Recipe('Oysters')

#Create Reviews
review1 = Review(stacy, recipe1, 5, 'Soup is too cold')
review2 = Review(stacy, recipe2, 4, 'My kids dont respect me')
review3 = Review(bob, recipe3, 3, 'I am happy')
review4 = Review(bob, recipe4, 1, 'YUM')
review5 = Review(bob, recipe5, 1, 'Yuck')

#Create Courses
course1 = Course(party1, recipe1)
course2 = Course(party1, recipe2)
course3 = Course(party1, recipe3)
