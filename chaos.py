#File: chaos.py
#A simple program illustrating chaotic behavior

def main():
    print("This program issustrates a chotic function")
    x = eval(input("Enter a number between 0 an 1: "))
    for i in range(10):
        x = 3.9 * x * (1 -x)
        print(x)
main()
