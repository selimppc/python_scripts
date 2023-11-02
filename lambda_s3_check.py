"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def twoSum(nums, target) -> list:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    pos = {target-n:i for i,n in enumerate(nums)}
    print('pos', pos)
    sol = next([i,pos[n]] for i,n in enumerate(nums) if i<pos.get(n,i))
    return sol

def main() -> None:
    """main"""
    nums = [2,7,11,15]
    target = 9

    result = twoSum(nums=nums, target=target)
    print(result)

if __name__ == "__main__":
    main()
