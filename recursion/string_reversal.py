#Task : Write a program that does string reversal using recursion concept

def reverse(input_string):
    if input_string == "":
        return input_string
    return reverse(input_string[1:])+ input_string[0]

if __name__ == "__main__":
    print(reverse("hellow"))