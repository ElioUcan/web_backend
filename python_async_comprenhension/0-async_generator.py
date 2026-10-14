#!/usr/bin/env python3

"""Module of asyncio comprenhension"""

import asyncio
import random
from typing import Iterartor


async def async_generator() -> Iterartor[float]:
    """Generates a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
