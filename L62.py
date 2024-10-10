#The author's name is Colleen
def find_perfect_number(x):
    if x <= 0:
        return False
    sum = 0
    if x > 0:
        for n in range(1,x):
            if x % n == 0:
                sum = sum + n
    if sum == x:
        return True
    else:
        return False

print(find_perfect_number(10000))
