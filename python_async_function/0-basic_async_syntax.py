#!/usr/bin/python3

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
