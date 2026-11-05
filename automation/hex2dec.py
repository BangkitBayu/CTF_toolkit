import argparse

parser = argparse.ArgumentParser(
	description="Convert hexadecimal to decimal"
)

parser.add_argument(
	"hex",
	help="Hexadecimal value (example: 0xFF or FF)"
)

args = parser.parse_args()

print("\n=== HEX TO DECIMAL CONVERTER ===")
try:
    result = int(args.hex, 16)
    print(f"Decimal: {result}")
except ValueError:
    print("Invalid hexadecimal input!")
