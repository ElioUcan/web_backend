#!/usr/bin/env python3

"""Imported differen coroutines"""

import asyncio
import time

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """total time divided by n"""
    return asyncio.create_task(wait_random(max_delay))
