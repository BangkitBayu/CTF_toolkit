# ==========================================
# IMPORT LIBRARY
# ==========================================

import argparse
import shutil
from pathlib import Path

# ==========================================
# CONFIGURATION
# ==========================================

# BASE DIRECTORY
BASE_DIR = Path("challenges")

import argparse
import shutil
from pathlib import Path


# ==========================================
# CONFIGURATION
# ==========================================

# Main directory for all your CTF
BASE_DIR = Path("challenges")

# ==========================================
# CREATE CHALLENGE FOLDER
# ==========================================

def create_challenge_dir(category, name):
	chall_dir = BASE_DIR/category/name
	
	chall_dir.mkdir(parents=True, exist_ok=True)
	
	print(f"[+] Challenge folder created: {chall_dir}")


def copy_challenge(source, category, name):
	source = Path(source)
	
	if not source.is_file():
		print("[-] Source file not found!")
		return
    
	chall_dir = BASE_DIR/category/name
	
	chall_dir.mkdir(parents=True, exist_ok=True)
	
	destination = chall_dir / source.name
	
	shutil.copy2(source, destination)
	
	print(f"[+] File copied successfully!")
	print(f"[+] Source      : {source}")
	print(f"[+] Destination : {destination}")
	
# ==========================================
# ARGUMENT PARSER
# ==========================================

parser = argparse.ArgumentParser(
    description="Simple CTF File Manager"
)

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

# ==========================================
# CMD: NEW
# ==========================================

new_parser = subparsers.add_parser(
    "new",
    help="Create a new challenge folder"
)

new_parser.add_argument("category")

new_parser.add_argument("name")

# ------------------------------------------
# CMD: COPY
# ------------------------------------------

copy_parser = subparsers.add_parser(
    "copy",
    help="Copy challenge file into workspace"
)

copy_parser.add_argument("source")

copy_parser.add_argument("category")

copy_parser.add_argument("name")

# ==========================================
# MAIN PROGRAM
# ==========================================

args = parser.parse_args()

match args.command:
	case "new":
	    create_challenge_dir(args.category, args.name)
	case "copy":
		copy_challenge(args.source,args.category,args.name)
	case _:
		print("UPS, Command not found")
