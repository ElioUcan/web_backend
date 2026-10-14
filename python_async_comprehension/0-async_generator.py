#!/usr/bin/env python3

"""Module of asyncio comprenhension inside a coroutine in python"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generates a random number waits 1 second and yields a random float"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
