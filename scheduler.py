# scheduler.py

import queue

class MLQScheduler:
    def __init__(self, num_queues):
        self.queues = [queue.PriorityQueue() for _ in range(num_queues)]
        self.processes = []

    def enqueue_process(self, process):
        initial_queue = min(process.priority, len(self.queues) - 1)
        self.queues[initial_queue].put(process)

    def run_simulation(self):
        time_elapsed = 0

        while any(not q.empty() for q in self.queues):
            for q_num, q in enumerate(self.queues):
                if not q.empty():
                    current_process = q.get()
                    print(f"Time {time_elapsed}: Running process {current_process.pid} from Queue {q_num} (Priority: {current_process.priority})")
                    current_process.remaining_time -= 1
                    current_process.wait_time += 1

                    if current_process.remaining_time > 0:
                        self.enqueue_process(current_process)
                    else:
                        print(f"Time {time_elapsed}: Process {current_process.pid} completed")

            # Aging Mechanism: Increase priority of waiting processes
            for q_num, q in enumerate(self.queues[:-1]):
                for process in list(q.queue):
                    if process.wait_time >= 3:
                        process.priority += 1
                        process.wait_time = 0
                        # Re-enqueue the process with the updated priority
                        self.queues[min(process.priority, len(self.queues) - 1)].put(process)

            time_elapsed += 1

    def display_queues(self):
        for q_num, q in enumerate(self.queues):
            print(f"Queue {q_num} (Priority {q_num}): {[process.pid for process in list(q.queue)]}")
