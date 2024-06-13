#!/usr/bin/env python3
"""
Module to demonstrate asynchronous generator in Python.

This module provides an asynchronous generator function `async_generator`
which yields random numbers between 0 and 10, pausing for 1 second
between each number.
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """
    Asynchronous generator that yields random float numbers.

    This function generates 10 random float numbers between 0 and 10,
    yielding one number at a time with a 1-second pause between each yield.

    Returns:
        Generator[float, None, None]: An asynchronous generator yielding
        random float numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Pause for 1 second
        yield random.uniform(0.0, 10)  # Yield a random float between 0 and 10
