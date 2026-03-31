class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack 
        res = [0] * len(temperatures) # all zeros 
        stack = [] # contains [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # stack not empty and last temp is less than present temp
                stackT, stackInd = stack.pop() # present temp, present temp index 
                res[stackInd] = i - stackInd 
            stack.append((t, i))
        
        return res 












        # brute force 
        res = []
        n = len(temperatures)

        for i in range(n): 
            count = 1
            j = i + 1
            while j < n:
                if temperatures[i] < temperatures[j]:
                    break 
                j += 1
                count += 1
            
            if j == n:
                count = 0
            else:
                count = count
            res.append(count)
        
        return res