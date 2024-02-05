class Solution:
    def isValid(self, s: str) -> bool:
        dq = collections.deque()
        opening = {'(': ')', '[': ']', '{' : '}'}
        for i in range(len(s)):
            if s[i] in opening.keys():
                dq.append(s[i])
            else:
                if len(dq) > 0:
                    if s[i] == opening[dq[-1]]:
                        dq.pop()
                    else:
                        return False
                else:
                    return False
        return len(dq) == 0       
