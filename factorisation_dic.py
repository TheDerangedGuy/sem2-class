#wap to take user input of a number and print its factorisation using dictionary where key is the prime factor and value is the count of that prime factor in the factorisation
n = int(input("Enter a number to factorise: "))
dict = {} 
for i in range(2, int(n**0.5) + 1):
     while n % i == 0:
        dict[i] = dict.get(i, 0) + 1
        n //= i
if n > 1:
    dict[n] = dict.get(n, 0) + 1    
print(f"The prime factorisation of {n} is: {dict}")    