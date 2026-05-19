/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        if (intervals.size() == 0) return 0;
        Collections.sort(intervals, (a, b) -> Integer.compare(a.start, b.start));
        PriorityQueue<Integer> endTimes = new PriorityQueue<>();
        for (Interval interval : intervals) {
            if (!endTimes.isEmpty() && interval.start >= endTimes.peek()) {
                endTimes.poll();
            }
            endTimes.offer(interval.end);
        }
        return endTimes.size();
    }
}
