# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we travserse the linkedin until we reach end 
        # when we reached end we point the end to dummy node making it as new head 
        # then we travel back once we have n we remove it and put back 
        # last node point to null 

        # step 1:
        # traverse the linkedin list but how do we keep the list wihtout losing the nodes?
        # based on hints we can usee fast and slow 
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy 

        for _ in range(n):
            fast = fast.next 

        while fast.next:
            fast = fast.next 
            slow = slow.next 

        slow.next = slow.next.next 

        return dummy.next

        
        