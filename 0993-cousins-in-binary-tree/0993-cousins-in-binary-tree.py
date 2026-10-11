from collections import deque

class Solution:
    def isCousins(self, root, x, y):
        q = deque([(root, None)])

        while q:
            size = len(q)
            x_parent = None
            y_parent = None
            x_found = False
            y_found = False

            for _ in range(size):
                node, parent = q.popleft()

                if node.val == x:
                    x_found = True
                    x_parent = parent
                if node.val == y:
                    y_found = True
                    y_parent = parent

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

            if x_found and y_found:
                return x_parent != y_parent

            if x_found or y_found:
                return False

        return False