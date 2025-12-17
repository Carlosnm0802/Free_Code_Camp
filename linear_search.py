def linear_search(arr,target):
    """Returns the index of the target if found in the array, else None."""
    for item in range(len(arr)):
        if arr[item] == target:
            return item
    return None
def verify(index):
    """Verifies the index is valid."""
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the array.")
number=[4,2,6,8,5,7,9,10]
result=linear_search(number,5)
verify(result)