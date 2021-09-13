def main():
    print( bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) )


def bubble_sort(input:list, ) -> list:
    n = len(input)
    for keep_passing in range(n - 1):
        for i in range(n - 1):
            if input[i] >= input [i + 1]:
                input[i], input[i + 1] = input[i + 1], input[i]
    
    return input

if __name__ == "__main__":
    # execute only if run as a script
    main()