def cal():
	num1=int(input("Enter a number: "))
	num2=int(input("Enter a number: "))
	choice=input("Enter your choice: ")
	if choice=='+':
		num=num1+num2
		print(num)
	if choice=='-':
		num=num1-num2
		print(num)
	if choice=='*':
		num=num1*num2
		print(num)
	if choice=='/':
		num=num1/num2
		print(num)
	if choice=='%':
		num=num1%num2
		print(num)
def main():
    cal()
if __name__== "__main__":
    main()

