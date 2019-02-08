def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def isPrimeInRange(start, end):
    primeList = [num for num in range(start, end) if isPrime(num) == True]
    return primeList