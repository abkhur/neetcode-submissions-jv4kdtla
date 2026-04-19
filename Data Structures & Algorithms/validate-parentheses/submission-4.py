class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      meow = { ")": "(", "]": "[", "}": "{" }

      for c in s:
        if c in meow:
            if stack and stack[-1] == meow[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
      return True if not stack else False  