def pattern(n):
    if n <= 0:
        return
    for i in range(n, 0, -1):
        leading = n - i
        stars = '*' * i
        print(' ' * leading + stars)
if __name__ == "__main__":
    pattern(5) 
    