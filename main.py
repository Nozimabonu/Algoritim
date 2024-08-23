arr = [10, 20, 30, 42, 11, 22, 56, 67, 89, 23, 44, 55, 66, 77]


# arr.sort()
# print(arr)

def linear_search(array: list, target: int):
    for arr in array:
        if arr == target:
            return array.index(arr)
    return -1


# print(linear_search(arr, 56))
# O(n)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(linear_search(arr, 10))

# push -->
# pop --> oxiridan oladi
# peek --> bunda ham chek qilinadi --> oxiridagi mikeni chiqardi
# is_empty -->
# size --> bu int tipidagilarni qayytaradi
# stack doc stack yozsa --> list tartibida chiqaradi --> stackni method
# pop_lif boshidan
# dequeue oxiridagi chiqib ketadi
# enqueue boshiga qo'shadi
# fiks bo'lsa yani o'zgaruvchan bo'lsa
# head --> har doim boshidan
#
