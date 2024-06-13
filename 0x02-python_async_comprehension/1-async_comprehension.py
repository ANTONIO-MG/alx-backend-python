#!/usr/bin/env python3
"""
Module to demonstrate the use of asynchronous comprehensions.

This module provides a function async_comprehension that collects
values from an asynchronous generator into a list using an
asynchronous list comprehension.
"""

import asyncio
from typing import List
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
    Collects values from the async_generator using asynchronous
    list comprehension.

    This function asynchronously iterates over the values produced
    by async_generator and collects them into a list.

    Returns:
        List[int]: A list of integers collected from the async_generator.
    """
    result: List[int] = [num async for num in async_generator()]
    return result
