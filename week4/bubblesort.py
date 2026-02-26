def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True
        if not swapped:
            break  
    return arr


def get_numbers_from_user():
    try:
        raw_input_data = input("Enter numbers separated by spaces: ").strip()
        if not raw_input_data:
            print("No input provided.")
            return []
        return [int(x) for x in raw_input_data.split()]
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return []


if __name__ == "__main__":
    numbers = get_numbers_from_user()
    if numbers:
        sorted_numbers = bubble_sort(numbers)
        print("Sorted list:", sorted_numbers)
