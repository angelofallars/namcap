"""Traverse through the whole repository, checking each PKGBUILD with namcap"""
import os
import sys

PROGRAM_NAME = "namcap"


def main():
    has_error = 0

    # Walk through the entire Git directory
    for present_dir, folders, files in os.walk("."):
        if "PKGBUILD" in files:
            pkgbuild_dir = os.path.join(present_dir, 'PKGBUILD')
            command = f"{PROGRAM_NAME} {pkgbuild_dir}"

            result = os.system(command)

            # If there's an error, the checker returns a non-zero value
            if result > 0:
                has_error = 1

    return has_error


if __name__ == "__main__":
    sys.exit(main())
