class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        elements = path.split("/")
        for el in elements:
            if el == "" or el == ".":
                continue
            else:
                if el == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(el)
            
        res = "/" + "/".join(stack)
        return res

        