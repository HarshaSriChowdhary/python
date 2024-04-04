class balance:
    def card(self):
        c=['rupay','visa','mastercard','1','2','3']
        while(1):
            card_type=input("enter type of card:\n 1.rupay\n 2.visa\n 3.mastercard\n")
            if card_type in c:
                break
            else:
                print("insert a valid card")
    def amount(self,a):
        print("The remaining balance is:",a)
obj=balance()
obj.card()
obj.amount(30000)
