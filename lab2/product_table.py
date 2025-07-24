def get_max():
    max_tries = 5
    while max_tries:
        max_num = input("Enter a number: ")
        if max_num.isdigit():
            max_num = int(max_num)
            break
        max_tries -= 1
    return max_num

def mult_table(max_num):
    product_table = []
    for i in range(1, max_num + 1):
        product_table.append([])
        for j in range(1, i + 1):
            product_table[i - 1].append(j * i)

    return product_table

def main():
    max_num = get_max()
    print(mult_table(max_num))

if __name__ == "__main__":
    main()