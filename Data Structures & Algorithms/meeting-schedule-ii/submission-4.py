class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])

        rooms = 0
        end_ptr = 0

        for start in starts:
            if start >= ends[end_ptr]:
                end_ptr += 1
            else:
                rooms += 1

        return rooms
