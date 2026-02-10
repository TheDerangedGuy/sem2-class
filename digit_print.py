#wap to print the number of digit of a user given number using function
def count_digits(n):
    if n == 0:
        return 1
    count = 0
    while n:
        n //= 10
        count += 1
    return count    
number = int(input("Enter a number: "))
print(f"The number of digits in {number} is {count_digits(abs(number))}.")