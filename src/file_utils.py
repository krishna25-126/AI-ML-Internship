"""
file_utils.py
Reusable functions for reading and writing simple CSV-style
text files without pandas. Useful for understanding what
pd.read_csv() does under the hood.
"""

def write_csv(path, header, rows):
    """Write a header and list of row-tuples to a CSV file."""
    with open(path, "w") as f:
        f.write(",".join(header) + "\n")
        for row in rows:
            f.write(",".join(str(item) for item in row) + "\n")

def read_csv(path):
    """Read a CSV file and return (header, rows) as lists."""
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    header = lines[0].split(",")
    rows = [line.split(",") for line in lines[1:]]
    return header, rows


if __name__ == "__main__":
    header = ["Name", "Marks"]
    rows = [("Asha", 88), ("Ravi", 72), ("Meera", 91)]

    write_csv("../data/day3_demo.csv", header, rows)

    header, rows = read_csv("../data/day3_demo.csv")
    print("Header:", header)
    for row in rows:
        print(row)
        