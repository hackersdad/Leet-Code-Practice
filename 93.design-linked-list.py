"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);   

"""

class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        
        if self.head is None or index >= self.length:
            return -1
        tracker = 0
        temp = self.head
        while temp:
            if index == tracker:
                return temp.val
            temp = temp.next
            tracker += 1
        
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.length:
            return
        if index == self.length:
            self.addAtTail(val)
            return

        if index == 0:
            self.addAtHead(val)
            return
        
        tracker = 1
        temp = self.head
        new_node = ListNode(val)
        while temp:
            if index == tracker:
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next
            tracker += 1
        self.length += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        
        if index >= self.length :
            return
        
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length = self.length - 1
            return

        tracker = 1
        temp = self.head
        while temp:
            if tracker == index:
                temp.next = temp.next.next if temp.next else None 
                if index == self.length-1:
                    self.tail = temp
                break
            temp = temp.next
            tracker += 1
        self.length = self.length - 1
        
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)