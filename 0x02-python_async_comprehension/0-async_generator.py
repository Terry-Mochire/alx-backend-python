#!/usr/bin/env python3

"""Async Generator"""

import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """Async Generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
