#lab1 to functions
def count_vowels(input_string):
    vowels = "aeiou"
    vowels += vowels.upper()
    n_vowels = 0
    for char in input_string:
        if char in vowels:
            n_vowels += 1

    return n_vowels

def mult_table(n):
    arr = []
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            arr.append(f"{i}x{j}={i*j}")

    return " , ".join(arr)

def find_i(input_string):
    locs = []

    for i in range(len(input_string)):
        if input_string[i] == "i":
            locs.append(i)

    return locs

def show_pyramid(max_stars):
    for i in range(max_stars):
        print(" " * (max_stars - i - 1) + "*" * (i + 1))

if __name__ == "__main__":
    print("Count Vowels")
    input_string = input("Enter a string: ")
    print(count_vowels(input_string))   
    print("-" * 20)
    print("Multiplication Table")
    n = int(input("Enter a number: "))
    print(mult_table(n))
    print("-" * 20)

    print("Find (i)s")
    input_string = input("Enter a string: ")
    print(find_i(input_string))
    print("-" * 20)

    print("Show Pyramid")
    max_stars = 5
    show_pyramid(max_stars)

