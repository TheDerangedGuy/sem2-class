def factorial(n):
	def f(n, a):
		return a if n <= 1 else f(n - 1, a * n)
	return f(n, 1)

if __name__ == "__main__":
	n = int(input("enter n: "))
	print(factorial(n))

