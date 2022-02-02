class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		n = len(nums)
		if n < 3:
			return []
		res = []
		nums.sort()  # O(nlogn)
		for i in range(n-2):  # O(n^2)
			if i == 0 or nums[i] != nums[i-1]:
				# 2Sum procedure...
				j = i+1
				k = n-1
				while j < k:
					sum = nums[i]+nums[j]+nums[k]
					if sum == 0:
						res.append([nums[i], nums[j], nums[k]])
						while j < k and nums[j] == nums[j+1]:
							j += 1
						while j < k and nums[k] == nums[k-1]:
							k -= 1
						j += 1
						k -= 1
					elif sum > 0:
						k -= 1
					else:
						j += 1
				# till here...
		# Time: O(nlogn)+O(n^2) = O(n^2)
		return res