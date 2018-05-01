#!/usr/bin/python3
import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.tokengenerator import TokenGenerator


def main():
    parser = argparse.ArgumentParser(description="Generate a firebase authentication token for a user.")
    parser.add_argument("email", type=str, help="The email to authenticate for.")
    args = parser.parse_args()

    generator = TokenGenerator()
    user = generator.get_token_for_email(args.email)
    print(user["idToken"])


if __name__ == '__main__':
    main()
