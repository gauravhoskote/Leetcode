class Solution:

    def f(self, nums, k):
        l = 0
        ctr = 0
        dd = {}
        vowels = ['a', 'e', 'i', 'o', 'u']
        for r in range(len(nums)):
            if nums[r] not in vowels:
                dd = {}
                continue
            else:
                if len(dd.keys()) == 0:
                    l = r
                dd[nums[r]] = dd.get(nums[r], 0)+1
                while len(dd.keys())>k:
                    if dd[nums[l]] == 1:
                        del dd[nums[l]]
                    else:
                        dd[nums[l]] -= 1
                    l+=1
                ctr += (r-l+1)
        return ctr            

    def countVowelSubstrings(self, word: str) -> int:
        return self.f(word, 5) - self.f(word, 4)
