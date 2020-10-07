import asyncio
import time
import random


def test_container_time(iters=500000):
    print("Starting script...")
    last_now = time.time()
    successful = True

    for i in range(iters):
        current_now = time.time()
        if current_now < last_now:
            print(f"Failed at iteration {i}")
            print(f"{current_now} < {last_now}")
            successful = False
            break

        last_now = current_now

        time.sleep(random.random() * 0.000001)

        if not i % 10000:
            print(f"Iteration {str(i)}")

    if successful:
        print("Completed successfully")

test_container_time()
