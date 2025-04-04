import argparse
from decimal_conversor import another_to_decimal, decimal_to_another

def main():
    parser = argparse.ArgumentParser(description="Converts a number between different bases. Optimized for power-of-2 bases (e.g., 2, 4, 8, 16).")

    parser.add_argument('number', type=str, help="The number to be converted.")
    parser.add_argument('original_base', type=int, help="The base in which the number is currently represented.")
    parser.add_argument('target_base', type=int, help="The base to convert the number into.")

    args = parser.parse_args()

    if args.original_base == 10:
        print(decimal_to_another(args.number, args.target_base))
        return

    if args.target_base == 10:
        print(another_to_decimal(args.number, args.original_base))
        return
    
    print(decimal_to_another(another_to_decimal(args.number, args.original_base), args.target_base))
    
if __name__ == "__main__":
    main()
        