# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head, algor='hash'):
        """
        Problem Description:
            A linked list is given such that each node contains an additional
            random pointer which could point to any node in the list or null.
            Return a deep copy of the list.
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        if algor == 'hash':
            node = head
            hash_bucket = {}
            """
            Step1. Just create new node, then store the corresponding relation between old and new in a dictionary
            {old_node_id: new_copied_node}
            Step2. For each old node, 
                   the corresponding new node's next node is equal to 
                                  the old one's next node's corresponding new node.
                   the corresponding new node's random node is equal to 
                                  the old one's random node's corresponding new node.    
            O(n) time complexity
            O(n) extra space complexity: hash table
            """
            while node:
                c_node = RandomListNode(node.label)
                hash_bucket[id(node)] = c_node
                node = node.next
            node = head
            while node:
                if node.next: hash_bucket[id(node)].next = hash_bucket[id(node.next)]
                if node.random:hash_bucket[id(node)].random = hash_bucket[id(node.random)]
                node = node.next
            return hash_bucket[id(head)]

        if algor == 'non_hash':
            """
               Step 1.   node1 ----------------->  node2 -----------------> node3
               Step 2.   node1 ---> cp_node1 --->  node2 ---> cp_node2 ---> node3 ---> cp_node3
               Step 3.   cp_node1.random = node1.random.next 
               Step 4.   reconstruct link-list, split copy_node and source node    
               Analysis: O(n) time complexity
                         O(1) extra space complexity 
            """
            node = head
            while node:
                temp = node.next
                copy = RandomListNode(node.label)
                node.next = copy
                copy.next = temp
                node = temp
            node = head
            while node:
                copy = node.next
                copy.random = node.random.next if node.random else None
                node = node.next.next
            node = head
            c_node = RandomListNode(0)
            pre_head = c_node
            while node:
                copy = node.next
                c_node.next = copy
                node.next = copy.next

                node = node.next
                c_node = c_node.next
            return pre_head.next



        # c_head = RandomListNode(head.label)
        # c_head.random = head.random
        # c_node = c_head
        # node = head.next
        # # copy
        # while node:
        #     c_node.next = RandomListNode(node.label)
        #     c_node = c_node.next
        #     c_node.random = node.random
        #     node = node.next
        # node = head
        # c_node = c_head
        # hash_bucket = {}
        # while node:
        #     hash_bucket[id(node)] = c_node
        #     # print("--------------")
        #     # print(id(node))
        #     # print(id(node.random))
        #     # print(id(node.next))
        #     # print("--------------")
        #     # print(id(c_node))
        #     # print(id(c_node.random))
        #     # print(id(c_node.next))
        #     # print("--------------")
        #     node = node.next
        #     c_node = c_node.next
        # c_node = c_head
        # while c_node:
        #     if c_node.random:
        #         c_node.random = hash_bucket[id(c_node.random)]
        #     c_node = c_node.next




# test
def print_link_list(head):
    node = head
    print("###########")
    while node:
        print("node is", node.label)
        if node.next: print("next is", node.next.label)
        else: print("next is", node.next)
        if node.random: print("random is", node.random.label)
        else: print("random is", node.random)
        print("###########")
        node = node.next

n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n1.next = n2
n1.random = n3
n2.next = n3
n2.random = n2
n3.next = None
n3.random = n1
s = Solution()
s.copyRandomList(n1)
# print_link_list(n1)
