class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answer = []
        for i in range(len(nums)):
            j = target-nums[i]
            if j in nums and nums.index(j) != i:
                answer.append(i)
                answer.append(nums.index(j))
                break

        return answer


#hash table

    def twoSumHash(self,nums: list[int], target:int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
