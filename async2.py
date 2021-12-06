import asyncio


async def handle_conection(reader, writer):
    print('connection made')
    while True:
        data = await reader.read(50)
        if data:
            data_len = len(data)
            print(f'received: {data_len}')
            writer.write(data)
            await writer.drain()
        else:
            print('closed')
            writer.close()
            break

# def run_handler():
loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.ensure_future(
        asyncio.start_server(handle_conection, '127.0.0.1', 15555), loop=loop
    )
)
loop.run_forever()
