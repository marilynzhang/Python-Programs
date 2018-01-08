def seq_search(array, value):
    for i in range(0, len(array)):
        if array[i] is value:
            return i
    return -1

def bin_search(array, value):
    left = 0
    right = len(array) - 1

    while (left <= right):
        middle = (left + right)/2
        if value > array[middle]:
            left =  middle + 1
        elif value < array[middle]:
            right = middle - 1
        else:
            return middle
    return -1

def bin_search_multi(array, value):
    left = 0
    right = len(array) - 1

    while (left <= right):
        middle = (left + right)/2
        if value > array[middle]:
            left =  middle + 1
        elif value < array[middle]:
            right = middle - 1
        else:
            answers = []
            for i in reversed(range(0, middle)):
                print i
                if array[i] == value:
                    answers.append(i)
                else:
                    break

            answers.append(middle)
            for i in range(middle + 1, len(array)):
                if array[i] == value:
                    answers.append(i)
                else:
                    break

            answers.sort()
            return answers
    return -1

#array = [8,6,4,7,9,4]
array = [4,4,4,4,4,4,4,4,4]
# print seq_search(array, 9)
# print seq_search(array, 4)
# print seq_search(array, 2)
# print bin_search(array, 9)
# print bin_search(array, 4)
# print bin_search(array, 2)
print bin_search_multi(array, 4)
