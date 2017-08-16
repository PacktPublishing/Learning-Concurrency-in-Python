import asyncio

class EchoServerProtocol(asyncio.Protocol):

  def connection_made(self, transport):
    peername = transport.get_extra_info('peername')
    print("Connection Made From {}".format(peername))
    self.transport = transport

  def data_received(self, data):
    message = data.decode()
    print("Data Received: {}".format(message))

    print("Send: {!r}".format(message))
    self.transport.write(data)

    print("Close the client socket")
    self.transport.close()


loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServerProtocol, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)

try:
  loop.run_forever()
except KeyboardInterrupt:
  pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()