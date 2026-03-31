class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # check the start and end?
        # [1, 2] and [2, 3] 
        # end 2 is matching with start 2 so we take less start and great end it would be 1 and 3 
        # how do we implment this in loop?
        # left and right pointer or for loop i , i +1 ?
        # how to sort by first value
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output