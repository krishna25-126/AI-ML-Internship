"""
list_stats.py
Compute basic descriptive statistics on a list of numbers,
without using external libraries. Good practice before using
Pandas/NumPy, which do this automatically.
"""

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def mode(numbers):
    counts = {}
    for n in numbers:
        counts[n] = counts.get(n, 0) + 1
    max_count = max(counts.values())
    modes = [n for n, c in counts.items() if c == max_count]
    return modes

def summary(numbers):
    return {
        "count": len(numbers),
        "mean": round(mean(numbers), 2),
        "median": median(numbers),
        "mode": mode(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }


if __name__ == "__main__":
    marks = [72, 85, 60, 91, 55, 72, 88, 72]
    print("Marks:", marks)
    for key, value in summary(marks).items():
        print(f"{key.capitalize()}: {value}")