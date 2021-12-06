import asyncio
from asyncio import transports


class EchoServer(asyncio.Protocol):
    def connection_made(self, transport: transports.BaseTransport) -> None:
        self.transport = transport
        print('connection made')

    def data_received(self, data: bytes) -> None:
        data_len = len(data)
        print(f'received: {data_len}')
        self.transport.write(data)

loop = asyncio.get_event_loop()
server = loop.create_server(EchoServer, '127.0.0.1', 15555)
loop.run_until_complete(server)
loop.run_forever()