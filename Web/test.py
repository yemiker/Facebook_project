# class Solution(object):
#     def twoSum(self, nums, target):
#       """
#       :type nums: List[int]
#       :type target: int
#       :rtype: List[int]
#       """
#       required = {}
#       for i in range(len(nums)):
#          if target - nums[i] in required:
#             return [required[target - nums[i]],i]
#          else:
#             required[nums[i]]=i
# input_list = [2,8,12,15]
# ob1 = Solution()
# print(ob1.twoSum(input_list, 20))

# class Solution(object):
#     def isPalindrome(self, x) -> bool:
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0: return False
#         div = 1
#         while x >= 10 * div:
#             div *= 10
#         while x:
#             if x // div != x % 10: return False
#             x = (x % div) // 10
#             div = div / 100
#         return True
# x = Solution()
# print(x.isPalindrome(122))







