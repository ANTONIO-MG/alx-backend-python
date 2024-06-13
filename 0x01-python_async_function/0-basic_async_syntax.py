#!/usr/bin/env python3
"""
Module to provide a coroutine for simulating a random delay.

This module provides a coroutine function wait_random that waits
for a random delay and then returns the delay duration.
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Waits for a random delay up to max_delay seconds and returns
    the delay duration.

    This coroutine generates a random float between 0 and max_delay,
    waits for that
    duration using asyncio.sleep, and then returns the delay.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The actual delay duration.
    """
    delay = random.uniform(0.0, max_delay)  # Generate a random delay
    await asyncio.sleep(delay)  # Wait for the delay duration
    return float(delay)  # Return the delay duration
