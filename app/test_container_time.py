from time import time


def test_container_time(iters=10000000):
    """Run a tight loop and test whether the current times across the iterations are non-decreasing"""

    print("Starting script...")

    last_now = time()
    successful = True

    for i in range(iters):
        # Get the current time
        current_now = time()

        # Check to see if the current time is before the time of the last iteration of this loop
        if current_now < last_now:
            print("Uh oh, we traveled back in time!")
            print(f"Failed at iteration {i}")
            print(f"Current time:\t{current_now}")
            print(f"Last time:\t{last_now}")
            print(f"Last time was {(last_now - current_now) * 1000} milliseconds ahead of this time.")
            successful = False
            break

        # Set the time of this iteration for comparison with the next
        last_now = current_now

        if not i % 100000:
            print(f"Iteration {str(i)}")

    if successful:
        print("Completed successfully.")

if __name__ == "__main__":
    test_container_time()
