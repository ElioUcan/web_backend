#!/usr/bin/env python3

"""Imported differen coroutines"""


import asyncio
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> list:
    """coroutines function"""
    task = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
