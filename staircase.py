def f(n):
	a=b=1
	for _ in range(n):
		a,b=b,a+b
	return a
if __name__ == "__main__":
	n = int(input("enter the number of stairs: "))
	print(f"There are {f(n)} ways")