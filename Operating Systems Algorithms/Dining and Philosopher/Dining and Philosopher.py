# import threading
# import time

# # Number of philosophers
# N = 5
# N = 5

# # Semaphore for each fork
# forks = [threading.Semaphore(1) for _ in range(N)]


# def philosopher(i):
#     while True:
#         # Think
#         print(f"Philosopher {i} is thinking")
#         time.sleep(1)

#         # Pick up left fork
#         forks[i].acquire()
#         print(f"Philosopher {i} picked up left fork")

#         # Pick up right fork
#         forks[(i+1) % N].acquire()
#         print(f"Philosopher {i} picked up right fork")

#         # Eat
#         print(f"Philosopher {i} is eating")
#         time.sleep(1)

#         # Put down left fork
#         forks[i].release()
#         print(f"Philosopher {i} put down left fork")

#         # Put down right fork
#         forks[(i+1) % N].release()
#         print(f"Philosopher {i} put down right fork")


# # Start the philosopher threads
# threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
# for thread in threads:
#     thread.start()

# # Run the simulation for 10 seconds
# time.sleep(10)

# # Stop the threads
# for thread in threads:
#     thread.join()

# # Print simulation complete message
# print("Simulation complete")


import threading
import time

# Number of philosophers
N = 5

# Semaphore for each fork
forks = [threading.Semaphore(1) for _ in range(N)]

# Mutex semaphore to protect the state of the forks
mutex = threading.Semaphore(1)

# State of the forks
fork_state = [True for _ in range(N)]


def philosopher(i):
    while True:
        # Think
        print(f"Philosopher {i} is thinking")
        time.sleep(1)

        # Pick up left fork
        mutex.acquire()
        if fork_state[i]:
            fork_state[i] = False
            forks[i].acquire()
            print(f"Philosopher {i} picked up left fork")
        else:
            # Release the mutex if left fork is not available
            mutex.release()
            continue

        # Pick up right fork
        if fork_state[(i+1) % N]:
            fork_state[(i+1) % N] = False
            forks[(i+1) % N].acquire()
            print(f"Philosopher {i} picked up right fork")
        else:
            # Release the left fork and mutex if right fork is not available
            fork_state[i] = True
            forks[i].release()
            mutex.release()
            continue

        # Release the mutex
        mutex.release()

        # Eat
        print(f"Philosopher {i} is eating")
        time.sleep(1)

        # Put down left fork
        forks[i].release()
        print(f"Philosopher {i} put down left fork")

        # Put down right fork
        forks[(i+1) % N].release()
        print(f"Philosopher {i} put down right fork")


# Start the philosopher threads
threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
for thread in threads:
    thread.start()

# Run the simulation for 10 seconds
time.sleep(10)

# Stop the threads
for thread in threads:
    thread.join()

# Print simulation complete message
print("Simulation complete")
