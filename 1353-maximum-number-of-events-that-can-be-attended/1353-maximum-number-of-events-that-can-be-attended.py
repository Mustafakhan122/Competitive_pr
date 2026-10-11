import heapq

class Solution:
    def maxEvents(self, events):
        # sort events by start day
        events.sort()
        heap = []   # min heap of end days
        i = 0
        n = len(events)
        day = 0
        ans = 0

        while i < n or heap:
            # if heap is empty, jump to the next event's start day
            if not heap:
                day = events[i][0]

            # add all events that start today
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # remove events that are already finished
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # attend the event that ends earliest
            if heap:
                heapq.heappop(heap)
                ans += 1
                day += 1

        return ans