# main.py

from process import Process
from scheduler import MLQScheduler

# Example usage with additional process for starvation
if __name__ == "__main__":
    process1 = Process(1, 0, 5)
    process2 = Process(2, 1, 3)
    process3 = Process(3, 2, 7)
    process_starvation = Process(4, 0, 10)

    scheduler = MLQScheduler(num_queues=3)
    scheduler.enqueue_process(process1)
    scheduler.enqueue_process(process2)
    scheduler.enqueue_process(process3)
    scheduler.enqueue_process(process_starvation)

    print("Initial Queues:")
    scheduler.display_queues()
    print("\nSimulation Output:")
    scheduler.run_simulation()
