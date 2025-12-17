def recursive_binary_search(list,target):
    if len(list)==0:
        return False
    else:
        mid=len(list)//2
        if list[mid]==target:
            return True
        elif list[mid]<target:
            return recursive_binary_search(list[mid+1:],target)
        elif list[mid]>target:
            return recursive_binary_search(list[:mid],target)
def verify(result):
    if result:
        print("Target found in the list")
    else:
        print("Target not found in the list")
#Examples
numbers=[10,20,30,40,50,60,70,80,90 ,100]
result=recursive_binary_search(numbers,70)
verify(result)
