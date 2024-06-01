class Node:
    """Linked list."""

    def __init__(self, value):
        self.next = None
        self.value = value


class Stack:
    """Stack class."""

    def __init__(self):
        self.top = Node("head")
        self.size = 0

    def push(self, value):
        """Push value to the top of the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Pop value from the top of the stack."""
        if self.is_empty:
            return Exception('Stack is empty')
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        """Return value from the top of the stack."""
        if self.is_empty:
            return Exception('Stack is empty')
        return self.top.value

    @property
    def is_empty(self):
        """Check if stack is empty."""
        return self.size == 0

    def get_size(self):
        """Return size of the stack."""
        return self.__len__()

    def __len__(self):
        """Return size of the stack."""
        return self.size

    def __str__(self):
        """Return string representation of the stack."""
        cur = self.top
        out = ''
        while cur is not None:
            out += str(cur.value) + '->'
            cur = cur.next
        return out[:-2]
