import asyncio

from bot.src.helperbot import main

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Exit')
    