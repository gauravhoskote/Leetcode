class Solution:
    def bestClosingTime(self, customers: str) -> int:
        arr = [0]*len(customers)
        c = 0
        for i in reversed(range(len(customers))):
            if customers[i] == 'Y':
                c += 1
            arr[i] = c
        c = 0
        sol = float('inf')
        sol_ind = -1
        for i in range(len(customers)):
            curr = arr[i] + c
            if curr < sol:
                sol_ind = i
                sol = curr
            if customers[i] == 'N':
                c += 1
        
        if c < sol:
            sol = c
            sol_ind = len(customers)

        return sol_ind
