def search_array(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("Element is found at position ", i)
        else:
            print("Oops! Element not found")


def main():
    arr = [1, 2, 3, 4, 5]
    key = 3
    search_array(arr, key)


if __name__ == '__main__':
    main()
