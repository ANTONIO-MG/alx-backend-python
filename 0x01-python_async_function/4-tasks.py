#!/usr/bin/env python3
"""
Module to execute tasks concurrently using asyncio.

This module provides a function task_wait_n which executes
multiple asynchronous
tasks concurrently and collects their results as they complete.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes n tasks concurrently with a maximum delay.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task in seconds.

    Returns:
        List[float]: A list of floats representing the delay of each
        completed task.
    """

    tasks: List[asyncio.Task] = []  # List to store the created tasks
    results: List[float] = []  # List to store the results

    # Create n tasks
    for _ in range(n):
        task: asyncio.Task = task_wait_random(max_delay)
        tasks.append(task)

    # Collect the results as they complete using list comprehension
    for task in asyncio.as_completed(tasks):
        result: float = await task
        results.append(result)

    return results
