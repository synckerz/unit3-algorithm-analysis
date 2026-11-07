def bubble_sort(numbers):
    n = len(numbers)

    for pass_number in range(n - 1):
        for i in range(n - 1 - pass_number):
            if numbers[i] > numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp

    return numbers


if __name__ == "__main__":
    numbers = [9, 4, 7, 1]
    print(bubble_sort(numbers))
