#The author's name is Colleen
x = 2
if x < 3:
    print("Small")

x = 5
if x < 3:
    print("Small")

score = 8 #A score on a 10 point quiz
if score > 6:
    print("Nice work!")

for i in range(1,16):
    if i % 3 == 0:
        print(i, "is divisible by 3.")

def is_even(x):
    if x % 2 == 0:
        print("Even")

is_even(4)
is_even(5)

x = 2
if x < 3:
    print("Small")
else:
    print("Large")

x = 5
if x < 3:
    print("Small")
else:
    print("Large")

score = 8 #A score on a 10 point quiz
if score < 6:
    print("Needs improvement")
elif score < 9:
    print("Nice work!")
else:
    print("Excellent!")

for i in range(-2,3):
    if i < 0:
        print(i, "is negative.")
    elif i == 0:
        print(i, "is zero.")
    else:
        print(i, "is positive.")

def iseven(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

iseven(2)
iseven(1)

print(3 < 4)
print(4 > 2)
print(type(True))

if True:
    print("This text will always appear.")
if False:
    print("This text will not appear.")

print(type(False))
print(3 == 5)

def is_greater_10(x):
    if x > 10:
        print(True)
    else:
        print(False)

is_greater_10(15)
is_greater_10(5)



