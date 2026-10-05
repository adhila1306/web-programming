y1=int(input("Enter starting year:"))
y2=int(input("Enter ending year:"))
if y1>y2:
    print("End year must be greater than or equal to start year")
else:
    print(f"Leap years from{y1} to {y2}")
    for Year in range(y1,y2+1):
        if(Year%4==0 and Year%100!=0)or (Year%400==0):
            print(Year)
