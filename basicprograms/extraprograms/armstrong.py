def armstrong(n):
	sum=0
	temp=n
	
	while temp>0:
		digit=temp%10
		sum+=digit**3
		temp//=10
	
	
	if(n==sum):
		print(f"{n} is armstrong")
	else:
		print(f"{n} not an armstrong")






n=int(input("enter number"))
armstrong(n)