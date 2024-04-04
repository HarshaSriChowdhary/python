def count(n):
    if n==0:
        return 0
    else:
        return 1+count(n//10)
count=count(153)
def arm(n,c):
    if n==0:
        return 0
    else:
        digit=n%10
        return digit**c+arm(n//10,count)
print(arm(153,count))
