def delete_element(arr, index):
    if index < 0 or index >= len(arr):
        print("Invalid index.")
        return arr

    del arr[index]
    return arr


array = [3, 7, 1, 9, 4]
index_to_delete = 2  
result = delete_element(array, index_to_delete)
print(result)
