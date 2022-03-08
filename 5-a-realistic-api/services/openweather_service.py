from typing import Optional
import httpx

api_key: Optional[str] = None


async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'

    url = f''
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    forecast = data['main']
    return forecast
