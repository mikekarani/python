def hello(): #creating a fx
    print("This is my first function")
hello()
hello()
hello()
hello()
def calculate():
    x=30
    y=56
    print(x*y)
calculate()

def majina(fname,lname):
    print(fname+""+lname)
majina("JOANNA", " FURAHA")
majina("maji", " tamu")
majina("uhai", " chungu")

def greetings(name, greeting="Hello"):
    print(greeting+""+name)
greetings(" majimiti")
greetings(" niaje", "joanna")
greetings(" joanna", "niaje")

def football(name,club):
    print(name+""+club)
football("messi"," barca")

#fx to return maximum value
def maxval(a, b, c, d, e, f):
    return max(a,b,c,d,e,f)
result=maxval(7,8,9,2,4,45)
print(result)

#fx to return minimum value
def minval(i,j,k,l,m,n,o,p):
    return min(i,j,k,l,m,n,o,p)
result=minval(0,45,54,67,1,87,85,100)
print(result)

#fx to sort numbers
def sort_list(lst):
    return sorted(lst)
answer=sort_list([3,9,0,2,7,1,5,4,2])
print(answer)

#fx to print out numbers
def print_numbers(n):
    for i in range(n):
        print(i)
    print_numbers(5)