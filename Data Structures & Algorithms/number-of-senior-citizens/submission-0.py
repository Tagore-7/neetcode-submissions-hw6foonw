class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for p in details:
            age = p[11:13]

            if int(age) > 60:
                count += 1

        return count
        