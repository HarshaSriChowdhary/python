#create a class ticket whuch will be the abstract class inside that create a function book ticket which will be the abstract method and has nothing in it.
#create a class make my trip which will use the book ticket function from ticket class to take the deatils osuch as name,phno,email,,journey date and displays a msg saying that thank you
#for booking from make my trip.
#create a class irctc which uses the book ticket of ticket class and takes the same details as make my trip but in the end it will give option to user to select whether it is 1 way or
#round trip.if the user option is round trip it again asks the user to enter return date as well and then prints a msg thank u for using irctc else it prints the msg thank for
#using irctc.create a class indigo which takes all the details as irctc and just asks which mode of transport you want to go in-train,flight,bus and displays thank you for choosing indigo

from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def bookticket(self):
        pass
class makemytrip(ticket):
    def bookticket(self):
        name=input("enter your name:")
        phno=input("enter phone number:")
        email=input("enter email id:")
        journeydate=input("enter journey date:")
    def display():
        print("Thank you for booking from make my trip")
class irctc(makemytrip):
    def bookticket1(self):    
        trip=input("enter the type of trip:\n 1.one way\n 2.round trip\n")
        if trip=="round trip":
            return_date=input("enter return date")
            print("thank you for choosing irctc")
        else:
            print("thank you for choosing irctc")
class indigo(irctc):
    def bookticket(self):
        mode=input("enter the mode of transport:\n 1.train\n 2.flight\n 3.bus\n")
        print("thank you for choosing indigo")
obj=makemytrip()
obj.bookticket()
obj.display()
obj1=irctc()
obj1.bookticket()
obj1.bookticket1()
obj2=indigo()
obj2.bookticket()

        
    
    
    
            
        
        
