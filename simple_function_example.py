


def add_two_numbers(a,b):
    return a + b

if __name__ == "__main__":
    print("hello world")
    n1 = int(input("enter number 1\n"))
    n2 = int(input("enter number 2\n"))
    # answer = multiply_two_numbers(n1,n2)
    answer = add_two_numbers(n1,n2)
    print(f"Those two numbers added is {answer}")
    #1. write a short summary of what a function is/does in python
    #2. write a function here called "multiply two number" that multiplies two numbers and prints the outpiut
    #python is an "interpreted" language - what does this mean?hjgcgnnvgh
     
if __name__ == "__main__":
    n1 = int(input("enter number 1"))
    n2 = int(input("enter number 2"))
    x = 5
    print(x)
    answer = multiply_two_numbers(n1,n2)
    print(f"Answer is {answer}")
    answer = add_two_numbers(n1,n2)
    print(f"Answer is {answer}")

def multiply_two_numbers(a,b):
        return a * b