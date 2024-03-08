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

########################################
# The Python Programming Language: BRIEF OOP
#An example of a class in python:
class Person:
    department = 'School of Information'  #a class variable
    # private ve protected olayı pythonda yoktur. Tam access var attribute ve methodlara.
    # explicit constructor'a ihtiyaç yoktur.
    # constructor tamılayacaksan =>  def __init__(self): şeklinde tanımlanır.
    def set_name(self, new_name):  #a method
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location

person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))


################### MAP FUNCTION #############
# Here's an example of mapping the min function between two lists.
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
cheapest
# map() => bize map object return eder.

#Now let's iterate through the map object to see the values.
for item in cheapest:
    print(item)

###############################################
#The Python Programming Language: LAMBDA FUNCTION
#Here's an example of lambda that takes in three parameters and adds the first two.
my_function = lambda a, b, c: a + b
my_function(1, 2, 3)

#Let's iterate from 0 to 999 and return the even numbers.
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
my_list

# Example
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

##################################################
#Now the same thing but with LIST COMPREHENSION
my_list = [number for number in range(0, 1000) if number % 2 == 0]
my_list

#example

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a + b + c + d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50]  # Display first 50 ids


#Example
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [j*i for i in range(10) for j in range(10)]

#NUMPY (numerical python lib)

# Numpy is the fundamental package for numeric computing with Python.
# It provides powerful ways to create, store, and/or manipulate data,
# which makes it able to seamlessly and speedily integrate with a wide variety of databases.
# This is also the foundation that Pandas is built on, which is a high-performance data-centric package.

#In here, we will talk about creating array with certain data types,
# manipulating array, selecting elements from arrays, and loading dataset into array.
# Such functions are useful for manipulating data and understanding the functionalities of other common Python data packages.

# we import a library using the `import` keyword as numpy's common abbreviation is np
import numpy as np
import math

#Array Creation
# Arrays are displayed as a list or list of lists and can be created through list as well. When creating an
# array, we pass in a list as an argument in numpy array
a = np.array([1, 2, 3])
print(a)
# We can print the number of dimensions of a list using the ndim attribute
print(a.ndim)
# If we pass in a list of lists in numpy array, we create a multi-dimensional array, for instance, a matrix
b = np.array([[1,2,3],[4,5,6]])
b
# We can print out the length of each dimension by calling the shape attribute, which returns a tuple
b.shape
# We can also check the type of items in the array
a.dtype
# Besides integers, floats are also accepted in numpy arrays
c = np.array([2.2, 5, 1.1])
c.dtype.name
# Let's look at the data in our array
c
# Note that numpy automatically converts integers, like 5, up to floats, since there is no loss of prescision.
# Numpy will try and give you the best data type format possible to keep your data types homogeneous, which
# means all the same, in the array.
# Sometimes we know the shape of an array that we want to create, but not what we want to be in it. numpy
# offers several functions to create arrays with initial placeholders, such as zero's or one's.
# Lets create two arrays, both the same shape but with different filler values
d = np.zeros((2,3))
print(d)

e = np.ones((2,3))
print(e)
# We can also generate an array with random numbers
np.random.rand(2,3)
# You'll see zeros, ones, and rand used quite often to create example arrays, especially in stack overflow
# posts and other forums.

# We can also create a sequence of numbers in an array with the arrange() function. The fist argument is the
# starting bound and the second argument is the ending bound, and the third argument is the difference between
# each consecutive numbers.
# Let's create an array of every even number from ten (inclusive) to fifty (exclusive)
f = np.arange(10, 50, 2)
f
# if we want to generate a sequence of floats, we can use the linspace() function. In this function the third
# argument isn't the difference between two numbers, but the total number of items you want to generate.
np.linspace( 0, 2, 15 ) # 15 numbers from 0 (inclusive) to 2 (inclusive)

#Array Operations

# We can do many things on arrays, such as mathematical manipulation (addition, subtraction, square,
# exponents) as well as use boolean arrays, which are binary values. We can also do matrix manipulation such
# as product, transpose, inverse, and so forth.
# Arithmetic operators on array apply elementwise.
a = np.array([10,20,30,40])
b = np.array([1, 2, 3,4])

# Now let's look at a minus b
c = a-b
print(c)

# And let's look at a times b
d = a*b
print(d)

# With arithmetic manipulation, we can convert current data to the way we want it to be. Here's a real-world
# problem I face - I moved down to the United States about 6 years ago from Canada. In Canada we use celcius
# for temperatures. With numpy I could easily convert a number of farenheit values, say the weather forecase, to ceclius.

# Let's create an array of typical Ann Arbor winter farenheit values
farenheit = np.array([0,-10,-5,-15,0])

# And the formula for conversion is ((°F − 32) × 5/9 = °C)
celcius = (farenheit - 31) * (5/9)
celcius

# Another useful and important manipulation is the boolean array. We can apply an operator on an array, and a
# boolean array will be returned for any element in the original, with True being emitted if it meets the condition and False oetherwise.
# For instance, if we want to get a boolean array to check celcius degrees that are greater than -20 degrees
celcius > -20

# Here's another example, we could use the modulus operator to check numbers in an array to see if they are even.
# Recall that modulus does division but throws away everything but the remainder (decimal) portion)
celcius%2 == 0

# Besides elementwise manipulation, it is important to know that numpy supports matrix manipulation. Let's
# look at matrix product. if we want to do elementwise product, we use the "*" sign
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
print(A*B)

# if we want to do matrix product, we use the "@" sign or use the dot function
print(A@B)

# A few more linear algebra concepts are worth layering in here. You might recall that the product of two
# matrices is only plausible when the inner dimensions of the two matrices are the same. The dimensions refer
# to the number of elements both horizontally and vertically in the rendered matricies you've seen here. We
# can use numpy to quickly see the shape of a matrix:
A.shape
# When manipulating arrays of different types, the type of the resulting array will correspond to
# the more general of the two types. This is called upcasting.

# Let's create an array of integers
array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1.dtype)

# Now let's create an array of floats
array2 = np.array([[7.1, 8.2, 9.1], [10.4, 11.2, 12.3]])
print(array2.dtype)

# Integers (int) are whole numbers only, and Floating point numbers (float) can have a whole number portion
# and a decimal portion. The 64 in this example refers to the number of bits that the operating system is
# reserving to represent the number, which determines the size (or precision) of the numbers that can be
# represented.

# Let's do an addition for the two arrays
array3=array1+array2
print(array3)
print(array3.dtype)
# Notice how the items in the resulting array have been upcast into floating point numbers

# Numpy arrays have many interesting aggregation functions on them, such as  sum(), max(), min(), and mean()
print(array3.sum())
print(array3.max())
print(array3.min())
print(array3.mean())

# For two dimensional arrays, we can do the same thing for each row or column
# let's create an array with 15 elements, ranging from 1 to 15,
# with a dimension of 3X5
b = np.arange(1,16,1).reshape(3,5)
print(b)
# Now, we often think about two dimensional arrays being made up of rows and columns, but you can also think
# of these arrays as just a giant ordered list of numbers, and the *shape* of the array, the number of rows
# and columns, is just an abstraction that we have for a particular purpose. Actually, this is exactly how
# basic images are stored in computer environments.

# Let's take a look at an example and see how numpy comes into play.
# For this demonstration we can use the python imaging library (PIL) and a function to display images in the
# Jupyter notebook
from PIL import Image
from IPython.display import display

# And let's just look at the image I'm talking about
im = Image.open('../chris.tiff')
display(im)
# Now, we can convert this PIL image to a numpy array
arr=np.array(im)
print(arr.shape)
arr
# Here we see that we have a 200x200 array and that the values are all uint8. The uint means that they are
# unsigned integers (so no negative numbers) and the 8 means 8 bits per byte. This means that each value can
# be up to 2*2*2*2*2*2*2*2=256 in size (well, actually 255, because we start at zero). For black and white
# images black is stored as 0 and white is stored as 255. So if we just wanted to invert this image we could
# use the numpy array to do so

# Let's create an array the same shape
mask=np.full(arr.shape,255)
mask
# Now let's subtract that from the modified array
modified_array=arr-mask

# And lets convert all of the negative values to positive values
modified_array=modified_array*-1

# And as a last step, let's tell numpy to set the value of the datatype correctly
modified_array=modified_array.astype(np.uint8)
modified_array
# And lastly, lets display this new array. We do this by using the fromarray() function in the python
# imaging library to convert the numpy array into an object jupyter can render
display(Image.fromarray(modified_array))

# Well, we could just decide to reshape the array and still try and render it.
# PIL is interpreting the individual rows as lines, so we can change the number of lines
# and columns if we want to. What do you think that would look like?
reshaped=np.reshape(modified_array,(100,400))
print(reshaped.shape)
display(Image.fromarray(reshaped))
# By reshaping the array to be only 100 rows high but 400 columns,
#  we've essentially doubled the image by taking every other line and stacking them out in width. This
# makes the image look more stretched out too.

# the point was to show you that these numpy arrays are really
# just abstractions on top of data, and that data has an underlying format (in this case, uint8). But further,
# we can build abstractions on top of that, such as computer code which renders a byte as either black or
# white, which has meaning to people. In some ways, this whole degree is about data and the abstractions that
# we can build on top of that data, from individual byte representations through to complex neural networks of
# functions or interactive visualizations. Your role as a data scientist is to understand what the data means
# (it's context an collection), and transform it into a different representation to be used for sensemaking.

#Indexing, Slicing and Iterating
#Indexing, slicing and iterating are extremely important for data manipulation and
# analysis because these techinques allow us to select data based on conditions, and copy or update data.

#Indexing
# First we are going to look at integer indexing. A one-dimensional array, works in similar ways as a list -
# To get an element in a one-dimensional array, we simply use the offset index.
a = np.array([1,3,5,7])
a[2]
# For multidimensional array, we need to use integer array indexing, let's create a new multidimensional array
a = np.array([[1,2], [3, 4], [5, 6]])
a
# if we want to select one certain element, we can do so by entering the index, which is comprised of two
# integers the first being the row, and the second the column
a[1,1] # remember in python we start at 0!
# if we want to get multiple elements
# for example, 1, 4, and 6 and put them into a one-dimensional array
# we can enter the indices directly into an array function
np.array([a[0, 0], a[1, 1], a[2, 1]])
# we can also do that by using another form of array indexing, which essential "zips" the first list and the
# second list up
print(a[[0, 1, 2], [0, 1, 1]])

#Boolean Indexing
# Boolean indexing allows us to select arbitrary elements based on conditions. For example, in the matrix we
# just talked about we want to find elements that are greater than 5 so we set up a conditon a >5
print(a >5)
# This returns a boolean array showing that if the value at the corresponding index is greater than 5
# We can then place this array of booleans like a mask over the original array to return a one-dimensional
# array relating to the true values.
print(a[a>5])

#Slicing
# Slicing is a way to create a sub-array based on the original array. For one-dimensional arrays, slicing
# works in similar ways to a list. To slice, we use the : sign. For instance, if we put :3 in the indexing
# brackets, we get elements from index 0 to index 3 (excluding index 3)
a = np.array([0,1,2,3,4,5])
print(a[:3])
# By putting 2:4 in the bracket, we get elements from index 2 to index 4 (excluding index 4)
print(a[2:4])

# For multidimensional arrays, it works similarly, lets see an example
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
a
# First, if we put one argument in the array, for example a[:2] then we would get all the elements from the
# first (0th) and second row (1th)
a[:2]
# If we add another argument to the array, for example a[:2, 1:3], we get the first two rows but then the
# second and third column values only
a[:2, 1:3]
# So, in multidimensional arrays, the first argument is for selecting rows, and the second argument is for
# selecting columns
# It is important to realize that a slice of an array is a view into the same data. This is called passing by
# reference. So modifying the sub array will consequently modify the original array

# Here I'll change the element at position [0, 0], which is 2, to 50, then we can see that the value in the
# original array is changed to 50 as well
sub_array = a[:2, 1:3]
print("sub array index [0,0] value before change:", sub_array[0,0])
sub_array[0,0] = 50
print("sub array index [0,0] value after change:", sub_array[0,0])
print("original array index [0,1] value after change:", a[0,1])


#Trying Numpy with Datasets
# Now that we have learned the essentials of Numpy let's use it on a couple of datasets
# Here we have a very popular dataset on wine quality, and we are going to only look at red wines. The data
# fields include: fixed acidity, volatile aciditycitric acid, residual sugar, chlorides, free sulfur dioxide,
# total sulfur dioxidedensity, pH, sulphates, alcohol, quality

# To load a dataset in Numpy, we can use the genfromtxt() function. We can specify data file name, delimiter
# (which is optional but often used), and number of rows to skip if we have a header row, hence it is 1 here.
# The genfromtxt() function has a parameter called dtype for specifying data types of each column this
# parameter is optional. Without specifying the types, all types will be casted the same to the more
# general/precise type

# Example Data-1
wines = np.genfromtxt("datasets/winequality-red.csv", delimiter=";", skip_header=1)
wines
# Recall that we can use integer indexing to get a certain column or a row. For example, if we want to select
# the fixed acidity column, which is the first column, we can do so by entering the index into the array.
# Also remember that for multidimensional arrays, the first argument refers to the row, and the second
# argument refers to the column, and if we just give one argument then we'll get a single dimensional list
# back.

# So all rows combined but only the first column from them would be
print("one integer 0 for slicing: ", wines[:, 0])
# But if we wanted the same values but wanted to preserve that they sit in their own rows we would write
print("0 to 1 for slicing: \n", wines[:, 0:1])

# If we want a range of columns in order, say columns 0 through 3 (recall, this means first, second, and
# third, since we start at zero and don't include the training index value), we can do that too
wines[:, 0:3]
# What if we want several non-consecutive columns? We can place the indices of the columns that we want into
# an array and pass the array as the second argument. Here's an example
wines[:, [0,2,4]]

# We can also do some basic summarization of this dataset. For example, if we want to find out the average
# quality of red wine, we can select the quality column. We could do this in a couple of ways, but the most
# appropriate is to use the -1 value for the index, as negative numbers mean slicing from the back of the
# list. We can then call the aggregation functions on this data.
wines[:,-1].mean()

# Example Data-2
# this time on graduate school admissions. It has fields such as GRE
# score, TOEFL score, university rating, GPA, having research experience or not, and a chance of admission.
# With this dataset, we can do data manipulation and basic analysis to infer what conditions are associated
# with higher chance of admission. Let's take a look.
# We can specify data field names when using genfromtxt() to loads CSV data. Also, we can have numpy try and
# infer the type of a column by setting the dtype parameter to None
graduate_admission = np.genfromtxt('datasets/Admission_Predict.csv', dtype=None, delimiter=',', skip_header=1,
                                   names=('Serial No','GRE Score', 'TOEFL Score', 'University Rating', 'SOP',
                                          'LOR','CGPA','Research', 'Chance of Admit'))
graduate_admission
# Notice that the resulting array is actually a one-dimensional array with 400 tuples
graduate_admission.shape

# We can retrieve a column from the array using the column's name for example, let's get the CGPA column and
# only the first five values.
graduate_admission['CGPA'][0:5]
# Since the GPA in the dataset range from 1 to 10, and in the US it's more common to use a scale of up to 4,
# a common task might be to convert the GPA by dividing by 10 and then multiplying by 4
graduate_admission['CGPA'] = graduate_admission['CGPA'] /10 *4
graduate_admission['CGPA'][0:20] #let's get 20 values

# Recall boolean masking. We can use this to find out how many students have had research experience by
# creating a boolean mask and passing it to the array indexing operator
len(graduate_admission[graduate_admission['Research'] == 1])

# Since we have the data field chance of admission, which ranges from 0 to 1, we can try to see if students
# with high chance of admission (>0.8) on average have higher GRE score than those with lower chance of admission (<0.4)
# So first we use boolean masking to pull out only those students we are interested in based on their chance
# of admission, then we pull out only their GPA scores, then we print the mean values.
print(graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8]['GRE_Score'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit'] < 0.4]['GRE_Score'].mean())

# When we do the boolean masking we are left with an array with tuples in it still, and numpy holds underneath
# this a list of the columns we specified and their name and indexes
graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8]
# Let's also do this with GPA
print(graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8]['CGPA'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit'] < 0.4]['CGPA'].mean())
# The GPA and GRE for students who have a higher chance of being admitted, at least based on our cursory look here,
# seems to be higher.

####################Regex###################
# Regular expressions, or regexes, are written in a condensed formatting language.
# In general, you can think of a regular expression as a pattern which you give to a regex processor with some source data.
# The processor then parses that source data using that pattern, and returns chunks of text back to the a data scientist
# or programmer for further manipulation. There's really three main reasons you would want to do this -
# 1) to check whether a pattern exists within some source data,
# 2) to get all instances of a complex pattern from some source data,
# 3) to clean your source data using a pattern generally through string splitting.
# Regexes are not trivial, but they are a foundational technique for data cleaning in data science applications,
# and a solid understanding of regexs will help you quickly and efficiently manipulate text data for further data science application.

# By the end of this lecture, you will understand the basics of regular expressions,
# how to define patterns for matching, how to apply these patterns to strings,
# and how to use the results of those patterns in data processing.

# First we'll import the re module, which is where python stores regular expression libraries.
import re
# There are several main processing functions in re that you might use. The first, match() checks for a match
# that is at the beginning of the string and returns a boolean. Similarly, search(), checks for a match
# anywhere in the string, and returns a boolean.

# Lets create some text for an example
text = "This is a good day."

# Now, lets see if it's a good day or not:
if re.search("good", text): # the first parameter here is the pattern
    print("Wonderful!")
else:
    print("Alas :(")
# In addition to checking for conditionals, we can segment a string. The work that regex does here is called
# tokenizing, where the string is separated into substrings based on patterns. Tokenizing is a core activity
# in natural language processing.

# The findall() and split() functions will parse the string for us and return chunks.
text = "Amy works diligently. Amy gets good grades. Our student Amy is successful."

# This is a bit of a fabricated example, but lets split this on all instances of Amy
re.split("Amy", text)
# You'll notice that split has returned an empty string, followed by a number of statements about Amy, all as
# elements of a list. If we wanted to count how many times we have talked about Amy, we could use findall()
re.findall("Amy", text)
# Ok, so we've seen that .search() looks for some pattern and returns a boolean, that .split() will use a
# pattern for creating a list of substrings, and that .findall() will look for a pattern and pull out all
# occurences.

#  The regex specification standard defines a markup language to describe patterns in text. Let's start with anchors.
# Anchors specify the start and/or the end of the string that you are trying to match. The caret character ^
# means start and the dollar sign character $ means end. If you put ^ before a string, it means that the text
# the regex processor retrieves must start with the string you specify. For ending, you have to put the $
# character after the string, it means that the text Regex retrieves must end with the string you specify.

# Here's an example
text = "Amy works diligently. Amy gets good grades. Our student Amy is successful."

# Let's see if this begins with Amy
re.search("^Amy",text)
# Notice that re.search() actually returned to us a new object, called re.Match object. An re.Match object
# always has a boolean value of True, as something was found, so you can always evaluate it in an if statement
# as we did earlier. The rendering of the match object also tells you what pattern was matched, in this case
# the word Amy, and the location the match was in, as the span. => <re.Match object; span=(0, 3), match='Amy'>

#################### Patterns and Character Classes ###################
# Let's talk more about patterns and start with character classes. Let's create a string of a single learners'
# grades over a semester in one course across all of their assignments
grades="ACAAAABCBCBAA"

# If we want to answer the question "How many B's were in the grade list?" we would just use B
re.findall("B",grades)

# If we wanted to count the number of A's or B's in the list, we can't use "AB" since this is used to match
# all A's followed immediately by a B. Instead, we put the characters A and B inside square brackets
re.findall("[AB]",grades) # ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A']

# This is called the set operator. You can also include a range of characters, which are ordered
# alphanumerically. For instance, if we want to refer to all lower case letters we could use [a-z] Lets build
# a simple regex to parse out all instances where this student receive an A followed by a B or a C
re.findall("[A][B-C]",grades) # ['AC', 'AB']

# Notice how the [AB] pattern describes a set of possible characters which could be either (A OR B), while the
# [A][B-C] pattern denoted two sets of characters which must have been matched back to back. You can write
# this pattern by using the pipe operator, which means OR
re.findall("AB|AC",grades) #  ['AC', 'AB']

# We can use the caret with the set operator to negate our results. For instance, if we want to parse out only
# the grades which were not A's
re.findall("[^A]",grades) # ['C', 'B', 'C', 'B', 'C', 'B']

# Note this carefully - the caret was previously matched to the beginning of a string as an anchor point, but
# inside of the set operator the caret, and the other special characters we will be talking about, lose their
# meaning. This can be a bit confusing. What do you think the result would be of this?
re.findall("^[^A]",grades) # []
# It's an empty list, because the regex says that we want to match any value at the beginning of the string
# which is not an A. Our string though starts with an A, so there is no match found. And remember when you are
# using the set operator you are doing character-based matching. So you are matching individual characters in
# an OR method.

#################### Quantifiers ###################
# Quantifiers are the number of times you want a pattern to be matched in order to match. The most basic
# quantifier is expressed as e{m,n}, where e is the expression or character we are matching, m is the minimum
# number of times you want it to matched, and n is the maximum number of times the item could be matched.

# How many times has this student been on a back-to-back A's streak?
re.findall("A{2,10}",grades) # we'll use 2 as our min, but ten as our max
# ['AAAA', 'AA']

# We might try and do this using single values and just repeating the pattern
re.findall("A{1,1}A{1,1}",grades)
# ['AA', 'AA', 'AA']
# As you can see, this is different than the first example. The first pattern is looking for any combination
# of two A's up to ten A's in a row. So it sees four A's as a single streak. The second pattern is looking for
# two A's back to back, so it sees two A's followed immediately by two more A's. We say that the regex
# processor begins at the start of the string and consumes variables which match patterns as it does.

# It's important to note that the regex quantifier syntax does not allow you to deviate from the {m,n}
# pattern. In particular, if you have an extra space in between the braces you'll get an empty result
re.findall("A{2, 2}",grades)

# And as we have already seen, if we don't include a quantifier then the default is {1,1}
re.findall("AA",grades)

# Oh, and if you just have one number in the braces, it's considered to be both m and n
re.findall("A{2}",grades)

# Using this, we could find a decreasing trend in a student's grades
re.findall("A{1,10}B{1,10}C{1,10}",grades) # ['AAAABC']

# Now, that's a bit of a hack, because we included a maximum that was just arbitrarily large.
# There are three other quantifiers that are used as short hand ;
# an asterix * to match 0 or more times,
# a question mark ? to match one or more times,
# or a + plus sign to match one or more times.

# Lets look at a more complex example, and load some data scraped from wikipedia
with open("datasets/ferpa.txt","r") as file:
    # we'll read that into a variable called wiki
    wiki=file.read()
# and lets print that variable out to the screen
wiki

# Scanning through this document one of the things we notice is that the headers all have the words [edit]
# behind them, followed by a newline character. So if we wanted to get a list of all of the headers in this
# article we could do so using re.findall
re.findall("[a-zA-Z]{1,100}\[edit\]",wiki)

# Ok, that didn't quite work. It got all of the headers, but only the last word of the header, and it really
# was quite clunky. Let's iteratively improve this. First, we can use \w to match any letter, including digits
# and numbers.
re.findall("[\w]{1,100}\[edit\]",wiki)
# This is something new. \w is a metacharacter, and indicates a special pattern of any letter or digit. There
# are actually a number of different metacharacters listed in the documentation. For instance, \s matches any
# whitespace character.

# Next, there are three other quantifiers we can use which shorten up the curly brace syntax. We can use an
# asterix * to match 0 or more times, so let's try that.
re.findall("[\w]*\[edit\]",wiki)
# Now that we have shortened the regex, let's improve it a little bit. We can add in a spaces using the space
# character
re.findall("[\w ]*\[edit\]",wiki)
# Ok, so this gets us the list of section titles in the wikipedia page! You can now create a list of titles by
# iterating through this and applying another regex
for title in re.findall("[\w ]*\[edit\]",wiki):
    # Now we will take that intermediate result and split on the square bracket [ just taking the first result
    print(re.split("[\[]",title)[0])

###################### Groups ########################
# Ok, this works, but it's a bit of a pain. To this point we have been talking about a regex as a single
# pattern which is matched. But, you can actually match different patterns, called groups, at the same time,
# and then refer to the groups you want. To group patterns together you use parentheses, which is actually
# pretty natural. Let's rewrite our findall using groups
re.findall("([\w ]*)(\[edit\])",wiki)
# We can actually refer to groups by
# number as well with the match objects that are returned. But, how do we get back a list of match objects?
# Thus far we've seen that findall() returns strings, and search() and match() return individual Match
# objects. But what do we do if we want a list of Match objects? In this case, we use the function finditer()
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.groups())
# We see here that the groups() method returns a tuple of the group. We can get an individual group using
# group(number), where group(0) is the whole match, and each other number is the portion of the match we are
# interested in. In this case, we want group(1)
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.group(1))
# One more piece to regex groups that I rarely use but is a good idea is labeling or naming groups. In the
# previous example I showed you how you can use the position of the group. But giving them a label and looking
# at the results as a dictionary is pretty useful. For that we use the syntax (?P<name>), where the parenthesis
# starts the group, the ?P indicates that this is an extension to basic regexes, and <name> is the dictionary
# key we want to use wrapped in <>.
for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])",wiki):
    # We can get the dictionary returned for the item with .groupdict()
    print(item.groupdict()['title'])
# Of course, we can print out the whole dictionary for the item too, and see that the [edit] string is still
# in there. Here's the dictionary kept for the last match
print(item.groupdict())

# Ok, we have seen how we can match individual character patterns with [], how we can group matches together
# using (), and how we can use quantifiers such as *, ?, or m{n} to describe patterns. Something I glossed
# over in the previous example was the \w, which standards for any word character. There are a number of
# short hands which are used with regexes for different kinds of characters, including:
# a . for any single character which is not a newline
# a \d for any digit
# and \s for any whitespace character, like spaces and tabs
# There are more, and a full list can be found in the python documentation for regexes

#################### Look-ahead and Look-behind ###################
# One more concept to be familiar with is called "look ahead" and "look behind" matching. In this case, the
# pattern being given to the regex engine is for text either before or after the text we are trying to isolate.

# For example, in our headers we want to isolate text which comes before the [edit] rendering, but
# we actually don't care about the [edit] text itself. Thus far we have been throwing the [edit] away, but if
# we want to use them to match but don't want to capture them we could put them in a group and use look ahead
# instead with ?= syntax
for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])",wiki):
    # What this regex says is match two groups, the first will be named and called title, will have any amount
    # of whitespace or regular word characters, the second will be the characters [edit] but we don't actually
    # want this edit put in our output match objects
    print(item)

#Example: Wikipedia Data
# Let's look at some more wikipedia data. Here's some data on universities in the US which are buddhist-based
with open("datasets/buddhist.txt","r") as file:
    # we'll read that into a variable called wiki
    wiki=file.read()
# and lets print that variable out to the screen
wiki
# We can see that each university follows a fairly similar pattern, with the name followed by an – then the
# words "located in" followed by the city and state

# I'll actually use this example to show you the verbose mode of python regexes. The verbose mode allows you
# to write multi-line regexes and increases readability. For this mode, we have to explicitly indicate all
# whitespace characters, either by prepending them with a \ or by using the \s special value. However, this
# means we can write our regex a bit more like code, and can even include comments with #
pattern="""
(?P<title>.*)        #the university title
(–\ located\ in\ )   #an indicator of the location
(?P<city>\w*)        #city the university is in
(,\ )                #separator for the state
(?P<state>\w*)       #the state the city is located in"""

# Now when we call finditer() we just pass the re.VERBOSE flag as the last parameter, this makes it much
# easier to understand large regexes!
for item in re.finditer(pattern,wiki,re.VERBOSE):
    # We can get the dictionary returned for the item with .groupdict()
    print(item.groupdict())

#Example: New York Times and Hashtags
# Here's another example from the New York Times which covers health tweets on news items. This data came from
# the UC Irvine Machine Learning Repository which is a great source of different kinds of data
with open("datasets/nytimeshealth.txt","r") as file:
    # We'll read everything into a variable and take a look at it
    health=file.read()
health
# So here we can see there are tweets with fields separated by pipes |. Let's try and get a list of all of the
# hashtags that are included in this data. A hashtag begins with a pound sign (or hash mark) and continues
# until some whitespace is found.

# So let's create a pattern. We want to include the hash sign first, then any number of alphanumeric
# characters. And we end when we see some whitespace
pattern = '#[\w\d]*(?=\s)'

# Notice that the ending is a look ahead. We're not actually interested in matching whitespace in the return
# value. Also notice that I use an asterix * instead of the plus + for the matching of alphabetical characters
# or digits, because a + would require at least one of each

# Let's search and display all of the hashtags
re.findall(pattern, health)
# We can see here that there were lots of ebola related tweeks in this particular dataset.




