#!/usr/bin/env python3
"""
Module to measure the execution time of concurrent tasks using asyncio.

This module provides a function measure_time to measure the
average execution time
of n asynchronous tasks executed concurrently.
"""

import time
import tracemalloc
import warnings
wait_n = __import__('1-concurrent_coroutines').wait_n

# Suppress RuntimeWarnings and start tracemalloc to monitor memory allocations
warnings.filterwarnings("ignore", category=RuntimeWarning)
tracemalloc.start()


def measure_time(n, max_delay):
    """
    Measures the average execution time of n asynchronous tasks
    with a maximum delay.

    This function calculates the time taken to execute n instances
    of the wait_n coroutine concurrently and returns the average time per task.

    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay for each task in seconds.

    Returns:
        float: The average time per task in seconds.
    """

    start_time = time.time()  # Record the start time
    # Call wait_n to execute n tasks concurrently with the specified max_delay
    wait_n(n, max_delay)

    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time  # Calculate the total elapsed time

    return elapsed_time / n  # Return the average time per task
