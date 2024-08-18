#HW_1
class Company:
     
     def __init__(self,Name,Address,SSN,size,empname,ssn,dob) :
          self.Name = Name
          self.Address = Address
          self.SSN = SSN
          self.obj[size] = Person(empname,ssn,dob)


class Person:

     def _init_(self,empName,SSN,DOB,size,Name,Address,ssn):
          self.empName = empName
          self.SSN = SSN
          self.DOB = DOB
          self.obj[size] =  Company(Name,Address,ssn)


#HW_2

class Author:

      def __init__(self,Name,BirthDate,NovelName,ReleasedDate):
           self.Name = Name
           self.BirthDate = BirthDate
           self.obj = Novel(NovelName,ReleasedDate)

      def Hello(self):
           print("My name is :"+self.Name+" and I born in : " + self.BirthDate)
           self.obj.Hello()

     


class Novel:

      def __init__(self,NovelName,ReleasedDate):
           self.NovelName = NovelName
           self.ReleasedDate = ReleasedDate
          
      def Hello(self):
           print("One of my novels is : "+ self.NovelName + " and the day it released : "+self.ReleasedDate)


author_1 = Author("Agatha Crestie","9/15/1890","And then there were none","11/6/1939") 

author_1.Hello()

#HW_3

class Father:

     def hello(self):
          print("Hi,here Father class")

class Child(Father):

     def hello(self):
          print("Hi,here Child class")


def fun(obj=Father): #here the expected argument is an object from father class , but it accepted the obj from child class because of the inheritance
     obj.hello()

C1 = Child()
fun(C1)     