# Reading and Writing CSV files

# Let's import our datafile mpg.csv, which contains fuel economy data for 234 cars.
#
# mpg : miles per gallon
# class : car classification
# cty : city mpg
# cyl : # of cylinders
# displ : engine displacement in liters
# drv : f = front-wheel drive, r = rear wheel drive, 4 = 4wd
# fl : fuel (e = ethanol E85, d = diesel, r = regular, p = premium, c = CNG)
# hwy : highway mpg
# manufacturer : automobile manufacturer
# model : model of car
# trans : type of transmission
# year : model year
import csv
# %precision 2

with open('datasets/mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

mpg[:3]  # The first three dictionaries in our list.

#csv.Dictreader has read in each row of our csv file as a dictionary. len shows that our list is comprised of 234 dictionaries.
len(mpg)

# keys gives us the column names of our csv.
mpg[0].keys()

# This is how to find the average cty fuel economy across all cars. All values in the dictionaries are strings, so we need to convert to float.
sum(float(d['cty']) for d in mpg) / len(mpg)

# Similarly this is how to find the average hwy fuel economy across all cars.
sum(float(d['hwy']) for d in mpg) / len(mpg)

#Use set to return the unique values for the number of cylinders the cars in our dataset have.
cylinders = set(d['cyl'] for d in mpg)
cylinders

#Here's a more complex example where we are grouping the cars by number of cylinder, and finding the average cty mpg for each group.
CtyMpgByCyl = []

for c in cylinders:  # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg:  # iterate over all dictionaries
        if d['cyl'] == c:  # if the cylinder level type matches,
            summpg += float(d['cty'])  # add the cty mpg
            cyltypecount += 1  # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount))  # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

# Use set to return the unique values for the class types in our dataset.
vehicleclass = set(d['class'] for d in mpg)  # what are the class types
vehicleclass

#And here's an example of how to find the average hwy mpg for each class of vehicle in our dataset.
HwyMpgByClass = []

for t in vehicleclass:  # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg:  # iterate over all dictionaries
        if d['class'] == t:  # if the cylinder amount type matches,
            summpg += float(d['hwy'])  # add the hwy mpg
            vclasscount += 1  # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount))  # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
HwyMpgByClass
# [('pickup', 16.88),
#  ('suv', 18.13),
#  ('minivan', 22.36),
#  ('2seater', 24.80),
#  ('midsize', 27.29),
#  ('subcompact', 28.14),
#  ('compact', 28.30)]

# The Python Programming Language: Dates and Times
import datetime as dt
import time as tm
# time returns the current time in seconds since the Epoch. (January 1st, 1970)
tm.time() # 1709715674.0148535
# Convert the timestamp to datetime.
dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow #datetime.datetime(2024, 3, 6, 12, 1, 53, 591775)

# Handy datetime attributes:
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second  # get year, month, day, etc.from a datetime

# timedelta is a duration expressing the difference between two dates.
delta = dt.timedelta(days=100)  # create a timedelta of 100 days
delta

# date.today returns the current local date.
today = dt.date.today()
today - delta  # the date 100 days ago
today > today - delta  # compare dates

# The Python Programming Language: Objects and map()
#An example of a class in python:
class Person:
    department = 'School of Information'  #a class variable

    def set_name(self, new_name):  #a method
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location

person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))

# Here's an example of mapping the min function between two lists.
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
cheapest

#Now let's iterate through the map object to see the values.
for item in cheapest:
    print(item)

#The Python Programming Language: Lambda and List Comprehensions
#Here's an example of lambda that takes in three parameters and adds the first two.
my_function = lambda a, b, c: a + b
my_function(1, 2, 3)

#Let's iterate from 0 to 999 and return the even numbers.
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
my_list

#Now the same thing but with list comprehension.
my_list = [number for number in range(0, 1000) if number % 2 == 0]
my_list