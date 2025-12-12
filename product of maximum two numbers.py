class Solution:
    def maxProduct(self, nums: list[int]) -> int:
       
        if len(nums) < 2:
            raise ValueError("Need at least two numbers")
        max1 = max2 = -10**18  
        for x in nums:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x
        return (max1 - 1) * (max2 - 1)

if __name__ == "__main__":
    s = Solution()
    tests = [
        ([3,4,5,2], 12),
        ([1,5,4,5], 16),
        ([3,7], 12),
    ]
    for arr, expected in tests:
        out = s.maxProduct(arr)
        print(f"nums = {arr} -> output = {out} (expected {expected})")
