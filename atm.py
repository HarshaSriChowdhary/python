#create an atm system.display the remaining amount in an atm.authentication of user.if the user is authenticated then give him the following options to choose 1)check balance 2)cash 
#withdrawl 3)cash deposit.mini statementof the last 3 transactions.rupay=2000,visa=5000,mastercard=8499
class atm:
    def authentication(self):
        name=input("enter name:")
        password=input("enter password:")
        if name==password:
            options=input("choose:\n 1.check balance\n 2.cash withdrawl\n 3.cash deposit\n 4.mini statement\n")                
        else:
             print("wrong credentials.please enter the details again")
             while(name!=password):
                 self.authentication()
                 break
obj=atm()
obj.options()
obj.authentication()
        
            
