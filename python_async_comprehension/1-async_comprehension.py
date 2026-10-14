#!/usr/bin/env python3

"""Module of prevouous task implementation"""

from typing import Generator

async_generator = __import__("0-async_generator").async_generator


async def asyunc_comprehension() -> Generator[float, None, None]:
    """Reutilizes the prevouous function"""
    return async_generator()
