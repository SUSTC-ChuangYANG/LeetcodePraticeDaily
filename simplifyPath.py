class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        return self.stack_simplify(path)

    @staticmethod
    def stack_simplify(path):
        path = list(path)
        stack_length = 0
        stack = []
        i = 0
        if path[len(path) - 1] == '/' and len(path) > 1:
            path.pop()
        while i < len(path):
            elem = path[i]
            if not stack:
                stack.append(elem)
                stack_length += 1
            else:
                top_elem = stack[stack_length - 1]
                if top_elem == '.' and elem == '/':
                    if path[i - 2] == '/':
                        stack.pop()
                        stack_length -= 1

                elif top_elem == '.' and elem == '.':
                    if (i == len(path) - 1 and path[i - 2] == '/') or (i != len(path) - 1 and path[i + 1] == '/'):
                        stack.pop()
                        stack.pop()
                        stack_length -= 2
                        if stack:
                            while stack[stack_length - 1] != '/':
                                stack.pop()
                                stack_length -= 1
                    else:
                        stack.append(elem)
                        stack_length += 1
                        i += 1
                        continue

                elif top_elem == '/' and elem == '/':
                    pass
                else:
                    stack.append(elem)
                    stack_length += 1

            i += 1

        if stack_length >= 2:
            if stack[stack_length - 1] == '.' and stack[stack_length - 2] == '/':
                stack.pop()
                stack.pop()
                stack_length -= 2
        if stack_length > 1:
            if stack[stack_length - 1] == '/':
                stack.pop()
        if not stack:
            return '/'

        return ''.join(stack)






s= Solution()
print(s.simplifyPath("/."))