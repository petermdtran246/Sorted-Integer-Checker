import sys

input_from_question = input().split()

def solution(input_from_question):
    #  Using map to convert string to integer
    nums = list(map(int, input_from_question))
    #  Check if the list of integers nums is sorted in ascending order
    return nums == sorted(nums)

print(solution(input_from_question))
