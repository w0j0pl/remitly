import argparse

from remitly.role_policy import verify_iam_role_policy


def main():
    parser = argparse.ArgumentParser(prog="remitly")
    parser.add_argument("filename", help="path to the JSON file, which you want to check")
    args = parser.parse_args()

    result = verify_iam_role_policy(args.filename)
    print(f"The return of the verify_iam_role_policy function is: {result}")


if __name__ == "__main__":
    main()

