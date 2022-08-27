from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def generate(stack=[], open=0, close=0):
            if len(stack) == n*2:
                output.append("".join(stack))
            if open<n:
                stack.append("{")
                generate(stack, open+1, close)
                stack.pop()

            if close<open:
                stack.append("}")
                generate(stack, open, close+1)
                stack.pop()
        generate()
        return output


if __name__ == "__main__":
    res = Solution().generateParenthesis(n=3)
    print(res)