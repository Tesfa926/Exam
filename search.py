def Search():
    n = int(input("Enter the number of elements: "))
    num_array = []
    for _ in range(n):
        num = int(input("Enter a number: "))
        num_array.append(num)

    search_num = int(input("Enter a number to search for: "))
    count = num_array.count(search_num)

    if count > 0:
        print(count)
    else:
        print("the number is not  in the array")

if __name__ == "__main__":
    Search()
