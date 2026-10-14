#!/usr/bin/env python3

"""Module of runtime for four parallel comprehensions"""

async_comprehension = __import__("async_comprehension").async_comprehension
import time
import asyncio


async def measure_time() -> float:
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return start - end
