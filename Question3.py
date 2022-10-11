# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a,b ='',''
        while(l1!=None):
            a+=str(l1.val)
            l1 = l1.next
        while(l2!=None):
            b+=str(l2.val)
            l2 = l2.next
        a,b = int(a[::-1]),int(b[::-1])
        ans = str(a + b)
        l = []
        for i in ans:
            l.append(int(i))
        l = l[::-1]
        res,temp = ListNode(l[0]),ListNode()
        temp = res
        for i in range(1,len(l)):
            temp.next = ListNode(l[i])
            temp = temp.next
        return res

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(2)
    l2.next = ListNode(0)
    l2.next.next = ListNode(4)
    answer = Solution()
    head_node = answer.addTwoNumbers(l1,l2)
    while(head_node!=None):
        print(head_node.val)
        head_node=head_node.next
        
# The Time complexity for this code is O(n).