fhand = open("mbox.txt", "r")
count = 0 
host = ""
for line in fhand:
    if line.startswith("From:"):
        line = line.rstrip()
        parts = line.split()
        if len(parts) >= 2:
            email = parts[1]
            if "@" in email:
                host = email.split("@")[1]
        print(host)
        count = count + 1
print('Total %d lines starts with "From:" ' % count)
fhand.close()
