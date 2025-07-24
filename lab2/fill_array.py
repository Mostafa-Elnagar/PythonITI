def sort_list():
    l = []
    for i in range(5):
        next_elm = input("Enter a number:")
        l.append(next_elm)

    print("Sorted list ascending:", sorted(l))
    print("Sorted list descending:", sorted(l, reverse=True))

if __name__ == "__main__":
    sort_list()