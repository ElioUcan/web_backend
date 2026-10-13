#!/usr/bin/env python3

"""module of asyncio"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Returns r"""
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
