fname = input("Enter a file name: ")
parts_value = 0
parts_sum = 0
parts_average = 0
parts_count = 0
try:
    fhand = open(fname,"r")
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:"):
            parts = line.split()
            parts_value = float(parts[1])
            parts_sum += parts_value
            parts_count += 1
    parts_average = parts_sum / parts_count
    print(f"Average spam confidence: {parts_average}")
except FileNotFoundError:
    print(f"File cannot be opened: {fname}")