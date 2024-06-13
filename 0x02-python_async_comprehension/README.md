# Asynchronous Python Modules

This repository contains a series of Python modules that demonstrate the use of asynchronous programming, including asynchronous generators and comprehensions, as well as measuring the runtime of concurrent tasks.

## Modules Overview

### 1. Asynchronous Generator (`0-async_generator.py`)

**Description:**
This module demonstrates an asynchronous generator in Python. The generator function `async_generator` yields random numbers between 0 and 10, pausing for 1 second between each number.

**Function:**
async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random float numbers.

    This function generates 10 random float numbers between 0 and 10,
    yielding one number at a time with a 1-second pause between each yield.

    Returns:
        Generator[float, None, None]: An asynchronous generator yielding
        random float numbers between 0 and 10.
    """



### 2. Asynchronous Comprehension (1-async_comprehension.py)

**Description:**
This module demonstrates the use of asynchronous comprehensions. The function async_comprehension collects values from an asynchronous generator into a list using an asynchronous list comprehension.

**Function:**
async def async_comprehension() -> List[int]:
    """
    Collects values from the async_generator using asynchronous
    list comprehension.

    This function asynchronously iterates over the values produced
    by async_generator and collects them into a list.

    Returns:
        List[int]: A list of integers collected from the async_generator.
    """

### 3. Measure Runtime (2-measure_runtime.py)
Description:
This module provides a function to measure the runtime of executing multiple asynchronous comprehensions concurrently. The function measure_runtime calculates the total execution time for running four instances of async_comprehension concurrently.

**Function:**
sync def measure_runtime() -> float:
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