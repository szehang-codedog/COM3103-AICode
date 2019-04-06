num = input("Enter no. of tickets: ")

def calc_fee(n):
    if n <= 5:
        return n * 100
    elif n>=6 and n<=10:
        return n*95
    elif n>=11:
        return n*90

print(calc_fee(num))
