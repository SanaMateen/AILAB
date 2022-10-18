def factorial(n):
	f=1
	if n==0:
		print(f"factorial of {n} is {f}")
	else:
		for i in range(1,n+1):
			f=f*i
		print(f"factorial of {n} is {f}")




n=int(input("enter the number"))
factorial(n)