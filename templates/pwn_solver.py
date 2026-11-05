from pwn import *
import argparse
import os

# ==========================================
# CONFIGURATION
# ==========================================

# File executable target

HOST = "127.0.0.1"
PORT = 1337

exe = "./chall" 
elf = ELF(exe)
context.binary = elf
context.arch = elf.arch
context.log_level = "info"

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
    
    """
    Function to run exploitation
    
    Writing your exploitation logic steps in here
    
    Parameter:
    io: connection
    """


# ==========================================
# MAIN
# ==========================================

def main():

    io = start()

    exploit(io)
    
    io.interactive()


if __name__ == "__main__":
    main()
