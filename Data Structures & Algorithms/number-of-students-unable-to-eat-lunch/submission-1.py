class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                result -= 1
                cnt[s] -= 1
            else:
                break
        return result