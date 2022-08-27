class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == "(":
                    if i != ")":
                        return False
                if current_char == "{":
                    if i != "}":
                        return False
                if current_char == "[":
                    if i != "]":
                        return False
        if stack:
            return False
        else:
            return True


if __name__ == "__main__":
    string = "()[]{}"
    valid = Solution()
    res = valid.isValid(s=string)
    print(res)