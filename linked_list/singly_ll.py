class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insertSLL(self, value, location):
            newNode = Node(value)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                if location == 0:
                    newNode.next = self.head
                    self.head = newNode
                elif location == -1:
                    newNode.next = None
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
                    if tempNode == self.tail:
                        self.tail=newNode
    
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def searchSLL(self, value):
        if self.head is None:
            print("The SLL does not exist")
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == value:
                    print("The value is at index:", index)
                    return node.value
                node = node.next
                index += 1
            print("The value is not in the SLL")
    
    def deleteNode(self, value):
        if self.head is None:
            print("The SLL does not exist")
        else:
            node = self.head
            if node.value == value:
                self.head = node.next
                if self.head is None:
                    self.tail = None
            else:
                while node is not None:
                    if node.next.value == value:
                        node.next = node.next.next
                        if node.next is None:
                            self.tail = node
                        return
                    node = node.next
                print("The value is not in the SLL")
    
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(5,-1)
singlyLinkedList.insertSLL(0, 0)

print([node.value for node in singlyLinkedList]) 

#print(singlyLinkedList.traverseSLL())

#print(singlyLinkedList.searchSLL(33))

singlyLinkedList.deleteNode(5)
singlyLinkedList.deleteNode(0)
singlyLinkedList.deleteNode(3)

print([node.value for node in singlyLinkedList]) 






