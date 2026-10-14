#!/usr/bin/env python3
"""Module that defines the async_comprehension coroutine."""


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> list[float]:
    """Collect 10 random numbers using an async comprehension
    over async_generator.
    """
    return [i async for i in async_generator()]
