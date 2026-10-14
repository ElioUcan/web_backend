#!/usr/bin/env python3
"""Module that measures the total runtime of async_comprehension."""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times concurrently using
    asyncio.gather and measure the total runtime.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
