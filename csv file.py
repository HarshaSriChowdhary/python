import csv
f=open("sri-csv",'a',newline="")
a=csv.writer(f)
a.writerow(["name","rollno","college","place"])
name=input("enter name:")
rollno=int(input("enter your roll number:"))
place=input("enter place:")
college=input("enter college name:")
a.writerow([name,rollno,college,place])
print("data has been saved")
          
                 
           