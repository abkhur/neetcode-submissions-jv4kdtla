from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr = arr1
    for i in range(len(arr2)):
        arr.append(arr2[i])
    return arr


def pop_n(arr: List[int], n: int) -> List[int]:
    ans = arr
    if n > len(ans):
        return []
    for i in range(n):
        ans.pop()
    return ans


def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    ans = arr
    ans.insert(index, element)
    return ans


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
