import argparse

parser = argparse.ArgumentParser(description="Converts a number between different bases. Optimized for power-of-2 bases (e.g., 2, 4, 8, 16).")

parser.add_argument('original_base', type=int, help="The base in which the number is currently represented.")
parser.add_argument('number', type=str, help="The number to be converted.")
parser.add_argument('target_base', type=int, help="The base to convert the number into.")

args = parser.parse_args()

print(args.original_base, args.number, args.target_base)
