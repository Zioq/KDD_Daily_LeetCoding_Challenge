def two_sum(nums: list, target: int) -> list:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    :param nums: a list of integers
    :param target: an integer
    :return: a list of indices of the two numbers such that they add up to target
    """
    return_list = []
    for index in range(len(nums)):
        for inner in range(index + 1, len(nums)):
            if nums[index] + nums[inner] == target:
                return_list.append(index)
                return_list.append(inner)
    if len(return_list) > 0:
        return return_list
    else:
        print("No two sum solution.")


# Another Solution (Less time complexity)
def two_sum_using_one_for_loop(nums: list, target: int) -> list:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    :param nums: a list of integers
    :param target: an integer
    :return: a list of indices of the two numbers such that they add up to target
    """
    temp = {}
    for index, value in enumerate(nums):
        remaining = target - value
        if remaining in temp:
            return [temp[remaining], index]
        else:
            temp[value] = index
    print("No two sum solution.")


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(two_sum(nums, target))

    nums = [3, 3]
    target = 6
    print(two_sum(nums, target))

    nums = [3, 3]
    target = 7
    print(two_sum(nums, target))

    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_using_one_for_loop(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(two_sum_using_one_for_loop(nums, target))

    nums = [3, 3]
    target = 6
    print(two_sum_using_one_for_loop(nums, target))

    nums = [3, 3]
    target = 7
    print(two_sum_using_one_for_loop(nums, target))


if __name__ == "__main__":
    main()
