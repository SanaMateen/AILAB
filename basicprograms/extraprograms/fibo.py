def fibo(n):
	x=0
	y=1
	z=0
	print(x,y,end="")
	for i in range(1,n):
		z=x+y
		x=y
		y=z
		print(z,end="")

fibo(4)