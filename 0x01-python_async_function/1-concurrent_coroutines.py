#!/usr/bin/env python3
"""
Module to execute multiple asynchronous tasks concurrently.

This module provides a function wait_n that creates and executes
n asynchronous tasks with a random delay.
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes n asynchronous tasks concurrently with random delays.

    This function creates n tasks that wait for a random delay between
    0 and max_delay seconds and collects their results as they complete.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task in seconds.

    Returns:
        List[float]: A list of floats representing the delay of each
        completed task.
    """

    tasks: List[asyncio.Task] = []  # List to store the created tasks
    results: List[float] = []  # List to store the resultss
    loop: int = 0  # Initialize the loop counter

    # Create n tasks with random delays
    while loop < n:
        delay: float = random.uniform(0.0, max_delay)
        tasks.append(asyncio.create_task(wait_random(delay)))
        loop += 1

    # Collect the results as they complete
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
