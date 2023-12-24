def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found in the list

my_list = list(map(int,input("Enter the list")))
target_value = int(input("Enter the number you need to find"))

result = linear_search(my_list, target_value)
if result != -1:
    print(f'Target {target_value} found at index {result}')
else:
    print(f'Target {target_value} not found')