import asyncio
import random


async def send_external_request(
    cadastral_number: str,
    latitude: float,
    longitude: float,
) -> bool:

    await asyncio.sleep(5)

    result = random.choice([True, False])

    return result
