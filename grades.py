grade=float(input("Enter your grade"))
if grade>=90:
    print("A")
elif grade<=89 and grade>=80:
    print("A-")
elif grade<=60 and grade>=88:
    print("B")
elif grade<=50 and grade>=35:
    print("C")
elif grade<=30 and grade>=49:
    print("D")
elif grade<=19 and grade>=29:
    print("E")
elif grade<=15and grade>=0:
    print("FAIL")
else:
    print("Reseat the paper")

