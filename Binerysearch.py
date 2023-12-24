def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  

my_list = list(map(int,input("Enter the list")))
target_value = int(input("Enter the number you need to find"))

result = binary_search(my_list, target_value)
if result != -1:
    print(f'Target {target_value} found at index {result}')
else:
    print(f'Target {target_value} not found')
