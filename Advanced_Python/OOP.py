# OOP-Object Oriented Programming-
# it is useful maintain, extend and write codes(by divide small pieces).
# Useful for repeatable, well-organized, memory-efficient codes.
# In python --> everything an object and they were created with class keyword.
# Also, we can create our objects by this way.
# Objects have methods, attributes that you can access with '.' format.

# naming convetion --> CamelCase
# Class => is a blueprint.
# CLASS -> instantiate process -> Instances (produced objects)
# class BigObject:
# 	#code
# 	pass

# obj1 = BigObject() # instantiating
# print(type(obj1)) # <class '__main__.BigObject'>

# ----------------------------
# CREATING OUR OWN OBJECT
# __init__() ==> Constructor/Init Method created with dunder way
'''
Note: Self refers to the object itself. So, self.name is nothing but player1.name
this way by using self, we pass the object itself to the class.
Every class method should have first argument as 'self'
and first method should be __init__ method.
'''
# class PlayerCharacter: # 'self === PlayerCharacter'
# 	membership = True # Class Object Attribute, it's an attribute of PlayerCharacter. It is a STATIC attribute.
#
# 	def __init__(self, name='anonymous', age=0):
# 		if self.membership: # or we can write: 'if PlayerCharacter.membership :
# 			self.name = name  # DYNAMIC Attribute or Property
# 			self.age = age
# 			print("I get printed at every instance created")
#
# 	def run(self):
# 		print(f"run method {self.name}")
# 		# print(f"run {PlayerCharacter.name})   # we cannot do this
#
# 	def shout(self, hello):
# 		print(f"{hello} I'm {self.name}")
#
#
# player1 = PlayerCharacter("jass", 22)
# print(player1)  # Memory location(unique for each obj) of the object
# print(player1.name)  # Notice that we are accessing the attributes, and hence we are not using
# # the parenthesis at the end
# print(player1.age)
# print(player1.run())    # Here we are accessing the method, and hence using parenthesis
# print(player1.shout('hii'))
# print(player1.membership)   # each of the class instance can access the class object attribute
# print(player2.membership)
#
# player2 = PlayerCharacter("togan", 98)
# player2.attack = True   # creating a new dynamic attribute for the player2
# print(player2.name)
# print(player2.age)
# print(player2.attack)

# player3 = PlayerCharacter() # object created with default parameters

# help(list) --> shows the blueprint of the class

# ----------------------------
# @classmethod & @staticmethod
# kinds of decorator
# @classmethod --> we can use this method without instantiating the class
# @staticmethod --> same as @classmethod, only thing is we don't pass the class as argument,
# and hence can't use its attribute

# class PlayerCharacter:
# 	membership = True
# 	def __init__(self, name, age):
# 		if age > 18:
# 			self.name = name
# 			self.age = age
# 	def run(self):
# 		print(f"run {self.name}")

# 	@classmethod
# 	def add_things(cls, n1, n2): # "cls" stands for CLASS
# 		return cls('Jojo', n1 + n2) # cls() => used as instantiation of PlayerCharacter

# 	@staticmethod
# 	def add_things2(n1, n2):
# 		return n1 + n2
#
# player1 = PlayerCharacter.add_things(14, 5)
# print(player1.name)
# print(player1.age)
# print(player1.membership)
#
# print(PlayerCharacter.add_things2(45, 5)) # 50
# print(player2.membership)     # gives error

# ----------------------------
# ENCAPSULATION
# The term states the process of binding the datas and the methods manipulating these datas to an Object.
# Actually, all the things we have done until this point.

# ABSTRACTION
# Hiding of information or abstracting of information getting accessed only one necessary.
# Private (_varname) Vs Public(varname) Variables
# class PlayerCharacter:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def run(self):
# 		print(f"run {self.name}")
#
# player1 = PlayerCharacter("Rohan", 22)
# player2 = PlayerCharacter("Mohan", 20)
#
# player1.name = "!!!!"
# player1.run = "BOOOO"
#
# print(player1.name)
# print(player1.run)
#
# print(player2.name)
# print(player2.run())
'''
Here the user has overwritten the class attributes and methods.
Which we would ideally don't want users to do.
However for other users, like player2, all the orginal attributes and methods functionality is intact.
Hence there is a need for Private attributes and methods, so the user cannot modify them.

But in Python the concept of Private is not there, so we have to work around that. 

So, we can use:
    class PlayerCharacter:
        def __init__(self, name, age):
            self._name = name  
            self._age = age
            
		def _run(self):  # PRIVATE METHOD
			print(f"run {self.name}")

    player1 = PlayerCharacter("Rohan", 22)
    player1.name = "!!!!" 

The user can still modify the attribute, by using 'player1._name = "!!!!"', but we are just letting him know
that '_name' is a private variable, and you should not change it.

It's a naming convention to start a private variable with '_' (an underscore), so other users will get to know about it.
Similarly we don't ever modify 'DUNDER/MAGIC' methods, they start and ends with two underscores (for eg. __init__)
'''
# ----------------------------
# INHERITANCE

# Parent Class
# class User:
#     def sign_in(self):
#         print("User is logged in.")
#
#
# # Sub Class/ Child Class/ Derived Class
# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attack(self):
# 	    print(f"{self.name} is attacking with {self.power} power.")
#
# Another Child Class
# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#
#     def attack(self):
#         print(f"{self.name} is attacking with {self.num_arrows} arrows.")
#
#     def check_arrows(self):
# 	    print(f"{self.num_arrows} arrows left.")
#
# Another Child Class with  Multiple Inheritance
# class HybridAttacker(Wizard, Archer):   # notice the order, in that order only it will give preference
#     def __init__(self, name, power, num_arrows):
#         Wizard.__init__(self,name,power)
#         Archer.__init__(self,name,num_arrows)
#
# wizard1 = Wizard('Merlin', 50)
# archer1 = Archer('Robbin', 100)
# hbot = HybridAttacker("Hydro", 50, 300)
#
# wizard1.attack()
# archer1.attack()
# hbot.attack()
# hbot.check_arrows()
# hbot.sign_in()
#
# print(hbot.name)
# print(hbot.power)
# print(hbot.num_arrows)
#
# print(isinstance(wizard1, Wizard)) # True
# print(isinstance(wizard1, User)) # True
# print(isinstance(wizard1, object)) # True
#
'''
By default every class is a subclass of 'object' class, hence when we type 'instance.' (object_name dot), we get all those
defualt methods suggestions from the IDE.
'''
# ----------------------------
# POLYMORPHISM
'''
 Polymorphism(many forms) --> Even though we are using the same function, it is giving different 
 output based on the object.
'''
# class User():
# 	def signed_in(self):
# 		print("User is logged in.")
#
# 	def attack(self):
# 		print("Do nothing.")
#
#
# class Wizard(User):
# 	def __init__(self, name, power):
# 		self.name = name
# 		self.power = power
#
# 	def attack(self):
# 		User.attack(self)  # Just a way to use parent class method.
# 		print(f"{self.name} is attacking with {self.power} power.")
#
#
# class Archer(User):
# 	def __init__(self, name, arrow):
# 		self.name = name
# 		self.arrow = arrow
#
# 	def attack(self): #Overriding the Parent Class method
# 		print(f"{self.name} is attacking with {self.arrow} arrows.")
#
#
# wizard1 = Wizard("John", 50)
# archer1 = Archer("Mohan", 85)
#
# def player_attack(char_):
#     char_.attack()#
#
# player_attack(wizard1)
# player_attack(archer1)
#
# for char in [wizard1, archer1]:
#     char.attack()

# # notice that these two instances are executing the child class method and not the parent class method.

# SUPER()
# class User():
# 	def __init__(self, email):
# 		self.email = email
# 	def signed_in(self):
# 		print("User is logged in.")
# 	def attack(self):
# 		print("Do nothing.")
#
# class Wizard(User):
# 	def __init__(self, name, power, email):
# 		self.name = name
# 		self.power = power
# 		super().__init__(email)  # same as using the below command, it does not take 'self' parameter
# 	    # User.__init__(self, email)
#
# 	def attack(self):
# 		print(f"{self.name} is attacking with {self.power} power.")
#
# wizard1 = Wizard("John", 50, 'john@gmail.com')
# print(wizard1.email)

# ----------------------------
# OBJECT INTROSPECTION
# print(dir(list))
'''
It gives us all the methods and attributes that the item has access to.
But we get this functionality with IDEs build in, when we type item or instance name dot for eg.list.
and then IDE will pop a window with all the methods and attributes it has access to.
'''
# ----------------------------
# DUNDER/MAGIC METHODS
