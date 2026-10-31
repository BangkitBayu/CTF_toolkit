from pwn import *
import argparse
import os

# ===================================
# Configuration
# ===================================

BINARY = "./chall"

HOST = "127.0.0.1"
PORT = 80

context.binary = ELF(BINARY)
context.arch = context.binary.arch
context.log_level = "info"

elf = context.binary

# ==========================================
# CONFIGURATION
# ==========================================

BINARY = "./chall"

HOST = "127.0.0.1"
PORT = 1337

context.binary = ELF(BINARY, checksec=False)
context.arch = context.binary.arch
context.log_level = "info"

elf = context.binary

# ==========================================
# ARGUMENT PARSER
# ==========================================

parser = argparse.ArgumentParser(
    description="Pwntools Solver"
)

parser.add_argument(
    "mode",
    choices=["local", "remote"],
    help="Execution mode"
)

args = parser.parse_args()

# ==========================================
# CONNECTION
# ==========================================

def start():

    if args.mode == "local":

        log.info("Starting local process")

        return process(BINARY)

    elif args.mode == "remote":

        log.info(f"Connecting to {HOST}:{PORT}")

        return remote(HOST, PORT)


# ==========================================
# EXPLOIT / SOLVER
# ==========================================

def exploit(io):

   #Exploit step

    pass


# ==========================================
# MAIN
# ==========================================

def main():

    io = start()

    exploit(io)

    io.interactive()


if __name__ == "__main__":
    main()
