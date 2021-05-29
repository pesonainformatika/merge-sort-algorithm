def merge_two_list(a: list, b: list) -> list:
    sorted_list = []
    length_a = len(a)
    length_b = len(b)

    # counter
    i = j = 0

    while i < length_a and j < length_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < length_a:
        sorted_list.append(a[i])
        i += 1

    while j < length_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list

def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # merging list
    left = merge_sort(left)
    right = merge_sort(right)

    # return sorting
    return merge_two_list(left, right)


if __name__ == '__main__':
    arrays = [10, 3, 5, 15, 7, 8, 23, 98, 29]
    print(merge_sort(arrays))
