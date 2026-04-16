import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    ans = strings
    heapq.heapify(ans)
    return ans


def heapify_integers(integers: List[int]) -> List[int]:
    ans = integers
    heapq.heapify(ans)
    return ans


def heap_sort(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    return [heapq.heappop(nums) for i in range(len(nums))]


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
