"""Week 09 Graded Challenges: File Reading, Writing and Exceptions.

Complete the four functions below. Replace pass with your code.
Return results; do not use input().
Keep names and parameters unchanged so the automated tests can call them.
"""



# Challenge 1 (File Reading): Count Lines
def count_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


# Challenge 2 (File Writing): Write Numbered Lines
def write_numbered_lines(filepath, lines):
    with open(filepath, "w", encoding="utf-8") as f:
        for number, text in enumerate(lines, start=1):
            f.write(f"{number}. {text}\n")


# Challenge 3 (Searching Files): Find Matching Lines
def find_matching_lines(filepath, keyword):
    keyword_lower = keyword.lower()
    with open(filepath, "r", encoding="utf-8") as f:
        return [
            line.rstrip("\r\n")
            for line in f
            if keyword_lower in line.lower()
        ]


# Challenge 4 (Exception Handling): Safe Read Integer
def safe_read_int(filepath, default=0):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return default
    