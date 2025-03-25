def find_min_max(arr, start, end):

    if start == end:
        return arr[start], arr[start]

    if end == start + 1:
        if arr[start] < arr[end]:
            return arr[start], arr[end]
        return arr[end], arr[start]

    middle = (start + end) // 2

    low1, high1 = find_min_max(arr, start, middle)
    low2, high2 = find_min_max(arr, middle + 1, end)

    return min(low1, low2), max(high1, high2)


def main():
    user_input = input("Digite os números separados por espaço: ")
    numbers = list(map(int, user_input.split()))
    minimum, maximum = find_min_max(numbers, 0, len(numbers) - 1)
    print(f"O menor valor é: {minimum}, e o maior valor é: {maximum}")


if __name__ == "__main__":
    main()
