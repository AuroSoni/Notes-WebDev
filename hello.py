print("Enter your name.")
name = input()
print(f"Hello {name}!")
def square(x):
    return x*x
for i in range(10):
    print("{} squared is {}".format(i,square(i)))
