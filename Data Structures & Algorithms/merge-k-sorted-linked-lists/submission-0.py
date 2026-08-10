# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        minHeap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))
        
        dummyNode = ListNode()
        prvNode = dummyNode
        
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            
            prvNode.next = node
            prvNode = node
            
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i,  node.next))
                
        return dummyNode.next