
def countingSort(arr):
    max_value = max(arr)
    n = len(arr)
    freq_arr = [0] * (max_value+1)
    sorted_array = [0] * n

    for num in arr:
        freq_arr[num] += 1

    for i in range(1, len(freq_arr)):
        freq_arr[i] = freq_arr[i] + freq_arr[i-1]

    for item in arr[::-1]:
        sorted_array[freq_arr[item] - 1] = item
        freq_arr[item] -= 1

    return sorted_array

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print(result)

