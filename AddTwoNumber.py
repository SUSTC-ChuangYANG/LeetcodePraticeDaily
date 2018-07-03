# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        currentNode = ListNode(0)
        currentNode2 = l2
        currentNode1 = l1

        carry_bit = 0
        while(True):
            if currentNode1!= None and currentNode2 !=None:
                source_bit = (currentNode1.val + currentNode2.val + carry_bit) % 10
                carry_bit = int((currentNode1.val + currentNode2.val + carry_bit) / 10)
                currentNode.next = ListNode(source_bit)
                currentNode = currentNode.next
                currentNode1 = currentNode1.next
                currentNode2 = currentNode2.next
            else:
                if currentNode1 == None and currentNode2 ==None:
                    if carry_bit:
                        currentNode.next = ListNode(carry_bit)
                    break
                elif currentNode1!=None:
                    source_bit = (currentNode1.val+ carry_bit) % 10
                    carry_bit = int((currentNode1.val+ carry_bit) / 10)
                    currentNode.next = ListNode(source_bit)
                    currentNode = currentNode.next
                    currentNode1 = currentNode1.next
                else:
                    source_bit = (currentNode2.val + carry_bit) % 10
                    carry_bit = int((currentNode2.val + carry_bit) / 10)
                    currentNode.next = ListNode(source_bit)
                    currentNode = currentNode.next
                    currentNode2 = currentNode2.next











        i = len(list3) - 1
        startNode = ListNode(list3[i])
        currentNode = startNode
        while i >= 1:
            i = i - 1
            currentNode.next = ListNode(list3[i])
            currentNode = currentNode.next

        return startNode




def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    s = Solution()
    s.addTwoNumbers(l1=l1, l2=l2)

if __name__ == "__main__":
    main()