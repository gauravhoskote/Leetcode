class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = deque()
        sol = ''
        for i in range(len(s)):
            if s[i] == '(':
                st.append((s[i], len(sol)))
                sol = sol + s[i]
            elif s[i] == ')':
                if st:
                    st.pop()
                    sol = sol + s[i]
            else:
                sol = sol + s[i]
        
        while st:
            index = st[-1][1]
            sol = sol[:index] + sol[index+1:]
            st.pop()
        return sol
