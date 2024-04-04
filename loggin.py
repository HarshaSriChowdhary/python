import csv
class randl:
    def registration(self,username,password,pincode,city,phnno):
        self.username=username
        self.password=password
        self.pin=pincode
        self.city=city
        self.phnno=phnno
    with open('e_commerce','a',newline=" ") as file:
        store=csv.writer(file)
        store.writerow([self.username,self.password,self.pincode,self.city,self.phnno])
    
    def login(self,username,password):
    with open('e_commerce','r',newline=" ") as file:
            read=csv.DicReader(file)
            for row in read:
                if row["username"]==username and row["password"]==password:
                    return True
    False