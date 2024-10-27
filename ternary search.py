def ternary_search(arr, left, right, x):
    if left <= right:
   # calculate two midpoints (mid1 and mid2) to divide the array into three equal parts.
        mid1 = left + (right - left)
        mid2 = right -(right - left)
  #check if the element x is located at mid1 or mid2.
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        if x < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, x)
        elif x > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, x)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)

    return -1

# Example usage
arr = [1, 5, 8, 12, 20, 26, 30, 36, 50, 58, 72, 90, 100]
x = 26
result = ternary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
