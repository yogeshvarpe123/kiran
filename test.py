# Linked List Implementation in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Insert after a node
    def insert_after_node(self, prev_node_data, data):
        temp = self.head
        while temp and temp.data != prev_node_data:
            temp = temp.next
        if not temp:
            print("Node not found")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # Delete by value
    def delete_by_value(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            print("Value not found")
            return
        prev.next = temp.next
        temp = None

    # Delete at position (0-based)
    def delete_at_position(self, pos):
        if self.head is None:
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        prev = None
        count = 0
        while temp and count != pos:
            prev = temp
            temp = temp.next
            count += 1
        if not temp:
            print("Position out of range")
            return
        prev.next = temp.next
        temp = None

    # Search for element
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Get length (iterative)
    def length_iterative(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Get length (recursive)
    def length_recursive(self, node):
        if not node:
            return 0
        return 1 + self.length_recursive(node.next)

    # Reverse linked list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    # Find middle node
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    # Detect cycle (Floyd’s Cycle Detection)
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Merge two sorted linked lists
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_after_node(10, 15)
    ll.print_list()  # 5 -> 10 -> 15 -> 20 -> None

    ll.delete_by_value(15)
    ll.print_list()  # 5 -> 10 -> 20 -> None

    ll.delete_at_position(1)
    ll.print_list()  # 5 -> 20 -> None

    print("Search 20:", ll.search(20))  # True
    print("Length (Iterative):", ll.length_iterative())
    print("Length (Recursive):", ll.length_recursive(ll.head))

    ll.reverse()
    ll.print_list()  # 20 -> 5 -> None

    print("Middle Node:", ll.find_middle())

    # Example merge
    l1 = LinkedList()
    l2 = LinkedList()
    for i in [1, 3, 5]:
        l1.insert_at_end(i)
    for i in [2, 4, 6]:
        l2.insert_at_end(i)

    merged_head = merge_sorted_lists(l1.head, l2.head)
    temp = merged_head
    print("Merged List:", end=" ")
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
