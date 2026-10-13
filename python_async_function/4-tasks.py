#!/usr/bin/env python3

"""Imported differen coroutines"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    """coroutines function"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return asyncio.creat_task(delays)
