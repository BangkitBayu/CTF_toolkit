# ==========================================
# IMPORT LIBRARY
# ==========================================

import argparse
import shutil
from pathlib import Path


# ==========================================
# CONFIGURATION
# ==========================================

# Lokasi penyimpanan lokal.
# Folder dibuat di direktori yang sama dengan script.
BASE_DIR = Path(__file__).resolve().parent / "my-ctf-writeups"

# Lokasi mount flashdisk.
USB_MOUNT = Path("/run/media/bangkit/Ventoy")

# Folder workspace di dalam flashdisk.
USB_DIR = USB_MOUNT / "my-ctf-writeups"


# ==========================================
# ARGUMENT PARSER
# ==========================================

parser = argparse.ArgumentParser(
    description="Simple CTF File Manager"
)

# Membuat subcommand: new dan copy.
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

new_parser.add_argument("source" , help="Challenge source (PicoCTF, Hackthebox, Tryhackme, etc.)")
new_parser.add_argument("category", help="Category challenge")
new_parser.add_argument("name", help="Challenge name")

new_parser.add_argument(
    "--usb",
    action="store_true",
    help="Save workspace to USB Flashdisk"
)


# ==========================================
# CMD: COPY
# ==========================================

copy_parser = subparsers.add_parser(
    "copy",
    help="Copy challenge file into workspace"
)

copy_parser.add_argument("file", help="Path to the source file")
copy_parser.add_argument("source",  help="Challenge source (PicoCTF, Hackthebox, Tryhackme, etc.)")
copy_parser.add_argument("category", help="Category challenge")
copy_parser.add_argument("name",  help="Challenge name")

copy_parser.add_argument(
    "--usb",
    action="store_true",
    help="Copy workspace to USB Flashdisk"
)


# ==========================================
# PARSE ARGUMENT
# ==========================================

# Baca argument yang diberikan melalui terminal.
args = parser.parse_args()

# Pilih lokasi penyimpanan berdasarkan argument.
if args.usb:

    # Pastikan flashdisk benar-benar ter-mount.
    if not USB_MOUNT.is_mount():
        parser.error(f"Flashdisk belum ter-mount: {USB_MOUNT}")

    storage = USB_DIR

else:
    storage = BASE_DIR


# ==========================================
# CREATE CHALLENGE FOLDER
# ==========================================

def create_challenge_dir(source,category, name, storage):

    # Susun direktori berdasarkan kategori dan nama challenge.
    chall_dir = storage/ source / category / name

    # Buat folder beserta parent directory.
    chall_dir.mkdir(parents=True, exist_ok=True)

    print("[+] Challenge folder created!")
    print(f"[+] Destination: {chall_dir}")


# ==========================================
# COPY CHALLENGE FILE
# ==========================================

def copy_challenge(file,source, category, name, storage):

    # Ubah lokasi file sumber menjadi objek Path.
    file_path = Path(file).expanduser()

    # Periksa apakah file sumber tersedia.
    if not file_path.is_file():
        print("[-] File not found!")
        return

    # Tentukan folder tujuan.
    chall_dir = storage/source / category / name

    # Buat folder tujuan jika belum tersedia.
    chall_dir.mkdir(parents=True, exist_ok=True)

    # Tentukan nama dan lokasi file tujuan.
    destination = chall_dir / file_path.name

    # Hindari menimpa file yang sudah ada.
    if destination.exists():
        print(f"[-] File already exists: {destination}")
        return

    # Salin file beserta metadata dasarnya.
    shutil.copy2(file_path, destination)

    print("[+] File copied successfully!")
    print(f"[+] Source      : {file_path}")
    print(f"[+] Destination : {destination}")


# ==========================================
# MAIN PROGRAM
# ==========================================

match args.command:

    case "new":
        create_challenge_dir(
			args.source,
            args.category,
            args.name,
            storage
        )

    case "copy":
        copy_challenge(
			args.file,
            args.source,
            args.category,
            args.name,
            storage
        )

    case _:
        print("Oops, command not found!")
