

def maximum_pairwise_product(numbers):
    dict = {"first_max": 0, "second_max": 0}

    for i in range(len(numbers)):
        if numbers[i] > dict["first_max"]:
            dict["first_max"] = numbers[i]
        elif numbers[i] > dict["second_max"]:
            dict["second_max"] = numbers[i]
    print(dict.values())


maximum_pairwise_product([7, 5, 14, 2, 8, 8, 5214213412, 1, 2, 3])
