# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        new_list = []
        for lst in lists:
            curr = lst
            while curr:
                new_list.append(curr.val)
                curr = curr.next

        new_list.sort()
        head = ListNode(new_list[0])
        curr = head 
        for num in new_list[1:]:
            newNode = ListNode(num)
            head.next = newNode
            head = head.next
        return curr