def square(x):
    return x*x

def main():
    print("Enter your name.")
    name = input()
    print(f"Hello {name}!")
    for i in range(10):
        print("{} squared is {}".format(i+1,square(i+1)))

if __name__ == "__main__":
    main()
    #if I'm currently running this file
    #only then execute the main() function.
