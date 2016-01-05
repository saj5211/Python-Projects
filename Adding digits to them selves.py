def sumDigits(N):
    return N and N%10 + sumDigits(N//10)