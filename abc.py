	
def sum(num1,num2):	
	num=num1+num2
	print(num)
def sub(num1,num2):
	num=num1-num2
	print(num)
def mul(num1,num2):
	num=num1*num2
	print(num)
def div(num1,num2):
	num=num1/num2
	print(num)
def mod(num1,num2):
	num=num1%num2
	print(num)

def main():
	num1=int(input("Enter a number: "))
	num2=int(input("Enter a number: "))
	choice=input("Enter your choice: ")
	
	if choice=='+':
		sum(num1,num2)
	elif choice=='-':
		sub(num1,num2)
	elif choice=='*':
		mul(num1,num2)
	elif choice=='/':
		div(num1,num2)
	elif choice=='%':
		mod(num1,num2)
if __name__== "__main__":
    main()

