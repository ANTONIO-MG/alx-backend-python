#!/usr/bin/env python3
"""
Module to execute tasks concurrently using asyncio.

This module provides a function task_wait_n which executes
multiple asynchronous
tasks concurrently and collects their results as they complete.
"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


# Import task_wait_random from the previous task
async def task_wait_n(n, max_delay):
    """
    Executes n tasks concurrently with a maximum delay.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task in seconds.

    Returns:
        list: A list of floats representing the delay of each completed task.
    """

    tasks = []  # List to store the created tasks
    results = []  # List to store the results of the completed tasks

    # Create n tasks
    for _ in range(n):
        task = (task_wait_random(max_delay))
        tasks.append(task)

    # Collect the results as they complete using list comprehension
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
