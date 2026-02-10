#wap to print the prime numbers out of list given by user and using for loop
l1 = list(map(int, input("Enter numbers separated by space: ").split()))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True                     
prime_numbers = [num for num in l1 if is_prime(num)]
print("Prime numbers in the list are:", prime_numbers)   