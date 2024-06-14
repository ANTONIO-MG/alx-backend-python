#!/usr/bin/env python3
"""
This module provides a function to measure the runtime of executing
multiple asynchronous comprehensions concurrently.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing four instances of the
    async_comprehension function concurrently.

    This function uses the asyncio.gather method to run four instances
    of async_comprehension concurrently. It measures the start and end
    times of the execution to calculate the total runtime.

    Returns:
        float: The total runtime in seconds for executing the four
        asynchronous comprehensions.
    """

    start_time = time.time()  # Record the start time

    # Run four instances of async_comprehension concurrently
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()  # Record the end time

    run_time = end_time - start_time  # Calculate the total runtime

    return run_time  # Return the total runtime
