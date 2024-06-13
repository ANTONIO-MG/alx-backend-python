#!/usr/bin/env python3
"""
Module to execute tasks concurrently using asyncio.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task for the wait_random coroutine with a
    specified maximum delay.

    Args:
        max_delay (int): The maximum delay in seconds for the
        wait_random coroutine.

    Returns:
        asyncio.Task: An asyncio Task object for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
