#!/usr/bin/env python3
"""Concurrent coroutines"""


import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Return the list of all delays"""
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
