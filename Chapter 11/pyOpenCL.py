import pyopencl as cl

print(cl.get_platforms())

for platform in cl.get_platforms():
  for device in platform.get_devices():
    print(device)