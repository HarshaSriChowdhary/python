#shift zeroes to last end

list=[2,0,1024,0,40,230,0]
list1=[]
for i in range(len(list)):
    if list[i]>0:
        list1.append(list[i])
for i in range(len(list)):
    if list[i]==0:
        list1.append(list[i])
print(list1)
        
        
        
    
