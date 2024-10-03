"""
Unpack binary file.
"""
import pickletools


def inspect_pickle(input_filename: str, output_filename: str):
    """
    Inspect the contents of a pkl file without executing.
    """

    with open(input_filename, "rb") as in_file:
        with open(output_filename, "w") as out_file:
            pickletools.dis(in_file, out_file)

    print("unpack complete")


input_file = "sample.pkl"
output_file = "contents.txt"

inspect_pickle(
    input_filename=input_file,
    output_filename=output_file
)
