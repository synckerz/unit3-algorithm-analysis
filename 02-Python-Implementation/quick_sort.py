def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]

    smaller = []
    equal = []
    larger = []

    for number in numbers:
        if number < pivot:
            smaller.append(number)
        elif number == pivot:
            equal.append(number)
        else:
            larger.append(number)

    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    numbers = [9, 4, 7, 1]
    print(quick_sort(numbers))
