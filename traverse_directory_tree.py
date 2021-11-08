"""Traverse through the whole repository, checking each PKGBUILD with namcap"""
import os
import sys

PROGRAM_NAME = "namcap"

RED = "\033[91m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[01m"
DARKGRAY = "\033[37m"
UNDERLINE = "\033[04m"

def main():
    has_error = 0

    # Walk through the entire Git directory
    for present_dir, folders, files in os.walk("."):
        if "PKGBUILD" in files:
            pkgbuild_dir = os.path.join(present_dir, 'PKGBUILD')
            command = f"{PROGRAM_NAME} {pkgbuild_dir}"

            print(f"Checking {DARKGRAY}{pkgbuild_dir}{RESET} ...")
            result = os.system(command)

            # If there's an error, the checker returns a non-zero value
            if result > 0:
                has_error = 1

            print()

    return has_error


if __name__ == "__main__":
    sys.exit(main())
