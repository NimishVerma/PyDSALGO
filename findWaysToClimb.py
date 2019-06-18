"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
"""

def findSteps(N, ways=[1,2]):
    if N == 0 or N==1:
        return 1
    else:
        return findSteps(N-1) + findSteps(N-2)


def DP_findSteps(N):
    nums = [0]*(N+1)
    nums[0] = 1
    nums[1] = 1
    for i in range(2,N+1):
        nums[i] = nums[i-1]+nums[i-2]
    return nums[N]

print(DP_findSteps(4))
