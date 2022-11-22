def merge_sort(string, start=0, end=None):
    if end is None:
        end = len(string)

    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(string, start, mid)
        merge_sort(string, mid, end)
        merge(string, start, mid, end)


def merge(string, start, mid, end):
    left = string[start:mid]
    right = string[mid:end]
    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            string[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            string[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            string[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first = list(first_string.lower())
    secound = list(second_string.lower())

    merge_sort(first, 0, len(first_string))
    merge_sort(secound, 0, len(second_string))

    first_string_sorted = ''.join(first)
    secound_string_sorted = ''.join(secound)

    if (first_string_sorted == '' or secound_string_sorted == ''):
        return (first_string_sorted, secound_string_sorted, False)

    return (
        first_string_sorted,
        secound_string_sorted,
        first_string_sorted == secound_string_sorted)
