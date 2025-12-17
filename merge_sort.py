def merge_sort(list):
    """
    Sorts a linked list in ascending order using the merge sort algorithm.
    Returns a new sorted linked list.
    Divide the midpoint of the list and divide into sublists
    Conquer by recursively sorting the sublists
    Combine the sorted sublists into one sorted list.
    """
    if len(list) <=1:
        return list
    left_half, right_half = split(list)
    left= merge_sort(left_half)
    right=merge_sort(right_half)
    return merge(left,right)

def split(list):
    """
    Divides the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """
    mid=len(list)//2
    left=list[:mid]
    right=list[mid:]
    return left, right