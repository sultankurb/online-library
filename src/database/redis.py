import redis.asyncio as aioredis


client = aioredis.Redis(host="localhost", port=6379,)
