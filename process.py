# process.py

import heapq

class Process:
    def __init__(self, pid, priority, burst_time):
        self.pid = pid
        self.priority = priority
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.wait_time = 0

    def __lt__(self, other):
        # Custom comparison for priority-based scheduling
        return self.priority < other.priority
