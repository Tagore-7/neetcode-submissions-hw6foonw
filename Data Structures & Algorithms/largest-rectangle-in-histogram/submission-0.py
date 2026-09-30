class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # divide and conquer 

        def maxRect(l, r, h):
            if l == r:
                return h[l]
            m = (l + r) // 2


            # left max 
            leftMax = maxRect(l, m, h)
            # right max 
            rightMax = maxRect(m + 1, r, h)
            # cross max
            crossmax = crossMax(l, r, m, h)

            return max(leftMax, rightMax, crossmax)


        def crossMax(l, r, m, h):
            # grow outward from the middle 
            # select the max heigth when growing 
            # update minH
            i = m
            j = m + 1

            minH = min(h[i], h[j])
            bestArea = minH * 2

            while i > l or j < r:
                # reached left
                if i == l:
                    j += 1
                    minH = min(minH, h[j])

                # reached rigth 
                elif j == r:
                    i -= 1
                    minH = min(minH, h[i])

                # max h btw l and r 
                elif h[i - 1] > h [ j + 1]:
                    i -= 1
                    minH = min(minH,h[i] )
                
                else:
                    j += 1
                    minH = min(minH, h[j])

                area = (j - i + 1) * minH
                bestArea = max(bestArea, area)

            return bestArea 


        return maxRect(0, len(heights) - 1, heights)