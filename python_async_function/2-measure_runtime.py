#!/usr/bin/env python3

"""Imported differen coroutines"""

import asyncio
from typing import List

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> List[float]:
    """total time divided by n"""
    total_time = sum([wait_n(n, max_delay) for _ in n])
    return total_time / n
