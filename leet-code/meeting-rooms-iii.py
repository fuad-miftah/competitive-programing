class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        waiting = []
        avail = [i for i in range(n)]
        held = [0] * n
        meetings.sort()
        for meet in meetings:
            while waiting and waiting[0][0] <= meet[0]:
                end, room = heappop(waiting)
                heappush(avail, room)

            if avail:
                room = heappop(avail)
                heappush(waiting, [meet[1], room])
            else:
                endTime, room = heappop(waiting)
                newEndTime = endTime + (meet[1] - meet[0])
                heappush(waiting, [newEndTime, room])
            held[room] += 1
        return held.index(max(held))
        