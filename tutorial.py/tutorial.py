import math
import time
import random
import os
import shutil
import messages as msg
from car import Car
from abc import ABC,abstractclassmethod
#----------------------Data Type----------------------#


# firs_name = "osama"
# second_name = "omari"
# full_name = firs_name +" "+ second_name
# print("Hello "+ full_name)

# age = 20
# age += 1
# print(age)
# print(type(age))
# #print(" your age is : "+age) error
# print("your age is: ",age)#or
# print("your age is: "+str(age))

# height = 250.7
# print("your height is: "+str(height)+"cm")
# print(type(height))

# human = True
# print("are you a human: "+str(human))
# print(type(human))

# name, age, male ="osama", 19 ,True

# print(name)
# print(age)
# print(male)

# ahmad = anas = mohammed = 20
# print(ahmad)
# print(anas)
# print(mohammed)

#name = "osama"
# print(len(name))
# print(name.find("s"))
#print(name.capitalize())
#print(name.upper())
# print(name.lower())
#print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
#print(name.replace("o","O"))
# print(name*3)

# x = 1
# y = 2.0
# z = "3"

# x = float(x)
# y = float(y)
# z = float(z)

# print(x)
# print(y)
# print(z*2)

# x = str(x)
# y = str(y)
# z = str(z)

# print(x)
# print(y)
# print(z*2)


#----------------------Input----------------------#


# name = input("what is your name: ")
# age = int(input("How old are you ? : "))
# height = float(input("How tall are you ? :"))
# print("Hello " + name)
# print("You are "+str(age)+" years old")
# print("your tall is "+str(height)+"cm")


#-------------------Math functions-------------------#


# pi = 3.14
# x = 1
# y = 2
# z = 3
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
#print(math.sqrt(pi))
# print(max(x,y,z))
# print(min(x,y,z))



#---------------------slicing the strings---------------------#



# name = "Osama Omari"
# first_name = name[0:5]
# second_name = name[6:]
# funky_name = name[::3]
# reversed_name = name[::-1]
# print(first_name)
# print(second_name)
# print(funky_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://facebook.com"
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])



#-------------------------If else statemens-----------------------#


# age = int(input("How old are you? : "))

# if age == 100:
#     print("you are a century year old")  

# elif age >= 18:
#     print("you are an adult")
  
# elif age <= 0:
#     print("you haven't born yet")

# else:
#     print("you are a child")    


# temp = int(input("what is the tempreture today? :"))

# if temp >= 0 and temp <= 30:
#     print("the tempreture is good today!\ngo outside")

# elif temp < 0 or temp > 30:
#     print("the tempreture is bad today\nstay inside")

# if not(temp >= 0 and temp <= 30):
#      print("the tempreture is bad today\nstay inside")

# elif not(temp < 0 or temp > 30):
#      print("the tempreture is good today!\ngo outside")


# --------------------Loop---------------------#


# name = ""

# while len(name) == 0:
#     name = input("Enter your name:")

# print("Hello "+name)

# for i in range(50,100+1,2):
#     print(i)

# for i in "Osama Omari":
#     print(i)

# for secoonds in range(10,0,-1):
#     print(secoonds)
#     time.sleep(1)
# print("Happy new year!")    


# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for i in range(columns):
#         print(symbol,end="")
#     print()    



# while True:
#     name = input("Enter your name?: ")
#     if name != "":
#         break 


# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i,end="")

# for i in range(1,21):
#     if i== 13:
#         pass
#     else:
#         print(i)


#----------------------List----------------------#


# food = ["pizza","burger","Mansaf","Shawarma"]

# food[0] = "zinger"

# food.append("ice cream")
# food.remove("burger")
# food.pop()
# food.insert(0,"cake")
# food.sort()
# food.clear()

# for x in food:
#     print(x)

# drinks = ["coffee","tea","cola"]
# dinner = ["pizza","burger","hotdog"]
# deserts = ["cake","ice cream"]

# food = [drinks,dinner,deserts]

# print(food[1][1])


#---------------------tuple---------------------#


# student = ("osama",19,"male")

# print(student.count("Osama"))
# print(student.index(19))

# for x in student:
#     print(x)

# if "osama" in student:
#     print("osama is here")   



#---------------------sets---------------------#


# utensils = {"fork","spoon","knife","knife"}
# dishes = {"bowl","plate","cup","knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)

# print(utensils.difference(dishes))
# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

# for x in dinner_table:
#     print(x)



#---------------------Dictionary---------------------#


# capitals = {"Jordan":"Amman",
#             "Saudi arabia":"Riyadh",
#             "Qatar":"Doha",
#             "UK":"London"}

# capitals.update({"Germany":"Berlin"})
# capitals.update({"UK":"Irbid"})
# capitals.pop("Saudi arabia")
# capitals.clear()


# print(capitals["Qatar"])
# print(capitals.get("USA"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#     print(key,value)



#---------------------Indexing---------------------#


# name = "osama Omari"

# if(name[0].islower()):
#     name = name.capitalize()

# first_name = name[:5].upper()
# last_name = name[6:].lower()
# last_character = name[-1]



# print(first_name)
# print(last_name)
# print(last_character)




#---------------------Functions---------------------#


# def hello(first_name,second_name,age):
#     print("Hello "+first_name+" "+second_name)
#     print("you are "+str(age)+" years old")
#     print("Have a nice day")


# myname = "Osama"
# mylastname = "Omari"
# hello(myname,mylastname,20)

# def multiply(number1,number2):
#     return number1 * number2

# x = multiply(7,7)

# print(multiply(5,6))
# print(x)

# def hello(first,middle,last):
#     print("Hello "+first+" "+middle+" "+last)

# hello(middle="Ra'ed",last="Al-Omari",first="Osama")


# print(round(abs(float(input("Enter a whole positive number: ")))))


#args

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(5,5,5))    

#kwargs

# def hello (**kwargs):
#     # print("Hello " + kwargs["first"] + " " + kwargs["last"])
#     print("hello",end=" ")
#     for key,value in kwargs.items():
#         print(value , end=" ")



# hello(title="Mr.", first = "Osama" , middle="Ra'ed", last = "Al-Omari")



#---------------------Format method---------------------#


# animal = "cow"
# item = "moon"

# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {0} jumped over the {1}".format(animal,item))
# print("The {animal} jumped over the {animal}".format(animal="cow",item="mooon"))

# text = "The {} jumped over the {}"
# print(text.format(animal,item))


# name = "osama"

# print("Hello, my name is {}. Nice to meet you".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))


# number = 1000

# print("the number pi is {:.2f}".format(number))
# print("the number is {:,}".format(number))
# print("the number is {:b}".format(number))
# print("the number is {:o}".format(number))
# print("the number is {:x}".format(number))
# print("the number is {:e}".format(number))
# print("the number is {:E}".format(number))



      
#---------------------Random method---------------------#


# x = random.randint(1,6)
# y = random.random()  # between 0 and 1

# mylist = ['rock','paper','scissors']
# z = random.choice(mylist)

# cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

# random.shuffle(cards)

# print(cards)



#---------------------exception handling---------------------#


# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
    
# except ZeroDivisionError as e:
#     print(e)
#     print("you cant divide by zero idiot!")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers idiot!")    
# except Exception as e:
#     print(e)
#     print("something went wrong :(")
# else:
#     print(result)
# finally:
#     print("This will always execute")



#---------------------File detection---------------------#


# path = "C:\\Users\\ORZOm\\Desktop\\folder"

# if os.path.exists(path):
#     print("that location exists")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a diretory")    

# else:
#     print("that location does not exist")


# try:

#     with open("text.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("that file was not found :(")

# text = "Yoooooooo\nThis is some text\nHave a good one\n "
# text2 = "Have a nice day\n see ya\n"

# with open('text.txt','w') as file:
#     file.write(text)

# with open('text.txt','a') as file:
#     file.write(text2)


# shutil.copyfile('text.txt','copy.txt') #src,dest



# source = "folder"
# destination = "c://Users//ORZOm//Desktop//fodler"


# try:
#     if os.path.exists(destination):
#         print("there is already file there")
#     else:
#         os.replace(source,destination)
#         print(source + " was moved")
# except FileNotFoundError:
#     print(source + " was not found")

# path = 'folder'

# try:
#     # os.remove(path)
#     # os.rmdir(path)
#     shutil.rmtree(path)
# except FileNotFoundError:
#     print("This file was not found")
# except PermissionError:
#     print('you do not have permission to delete that')
# except OSError:
#     print("You cannot delete that usting that function")


# else:
#     print(path + " was deleted")



#---------------------Modules---------------------#

# msg.hello()
# msg.bye()

# or you can do it like this: from messages import * (or the name of the functions you want to use )
# then you can call the method without the messages
# you can check on the modules like this: help("modules")




#---------------------Object Orientd Programming---------------------#


# car_1 = Car("chevy","Corvette",2022,"black")
# car_2 = Car("Ford","Mustang",2022,"black")

# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)

# Car.wheels = 2

# print(car_1.wheels)
# print(car_2.wheels)



# car_1.drive()
# car_2.stop()



#---------------------Inheritance---------------------#



# class Animal:
 
#     alive = True

#     def eat(self):
#         print("This animla is eating")


#     def sleep(self):
#         print("This animal is sleeping")


        


# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running")
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")
# class Hawk(Animal):
#     def fly(self):
#         print("this hawk is flying")

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# rabbit.run()
# fish.swim()
# hawk.fly()


#---------------------multilevel inheritance---------------------#



# class Organism:

#     alive = True


# class Animal(Organism):

#     def eat(self):
#         print("This animal is eating")


# class Dog(Animal):
#     def bark(self):
#         print("This dog is barking")



# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()



#---------------------multiple inheritance---------------------#



# class Prey:

#     def flee(self):
#         print("This animal flees")


# class Predator:
#     def hunt(self):
#         print("This animal is hunting")



# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey,Predator):
#     pass



# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()



#---------------------Overriding---------------------#


# class Animal():

#     def eat(self):
#          print("This animal is eating")



# class Rabbit(Animal):
#     def eat(self):
#         print("This rabbit is eating carrot")
    

# rabbit = Rabbit()
# rabbit.eat()




#---------------------method chaining---------------------#


# class Car:

#     def turn_on(self):
#         print("You start the car")
#         return self
    
#     def drive(self):
#         print("You drive the car")
#         return self
    
#     def brake(self):
#         print("You step on the brakes")
#         return self
    
#     def turn_off(self):
#         print("You turn off the car")
#         return self
    

# car = Car()

# car.turn_on()\
# .drive()\
# .brake()\
# .turn_off()



#---------------------super function---------------------#


# class Rectangle:


#     def __init__(self,length,width) :
#         self.length = length
#         self.width = width


         
# class Square(Rectangle):

#     def __init__(self, length, width):
#         super().__init__(length, width)


#     def area(self):
#         return self.length*self.width


# class Cube(Rectangle):

#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height


#     def volume(self):
#         return self.length*self.width*self.height



# square = Square(3, 3)
# cube = Cube(3, 3, 3)

# print(square.area())
# print(cube.volume())



#---------------------abstract class---------------------#



# class Vehicle(ABC):
#     @abstractclassmethod
#     def go(self):
#         pass

#     @abstractclassmethod   
#     def stop(self):
#         pass


# class Car(Vehicle):
#     def go(self):
#         print("You drive the car")
#     def stop(self):
#         print("This car is stopped")

# class Motorcycle(Vehicle):
#     def go(self):
#         print("You ride the motorcycle")
#     def stop(self):
#         print("This motorcycle is stopped")


# #vehicle = Vehicle() #EROR
# car = Car()
# motor = Motorcycle()

# car.go()
# motor.go()
# car.stop()
# motor.stop()




#---------------------Objects as arguments---------------------#


# class Car:

#     color= None

# class Motorcylce:

#     color = None


# def change_color(Vehicle,color):
#     Vehicle.color = color


# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
# motor = Motorcylce()

# change_color(car_1,"Black")
# change_color(car_2,"White")
# change_color(car_3,"Red")
# change_color(motor,"Silver")

# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(motor.color)




#---------------------warlus operator---------------------#

# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)


#---------------------fuctions to variables---------------------#

# say = print
# say("wow")



















































