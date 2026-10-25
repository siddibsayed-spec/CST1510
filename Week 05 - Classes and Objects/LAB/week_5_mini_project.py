"""
RECORD CHECK  -  my version
===========================

Name  :siddiqah sayed 
Lane  : Cyber 
Date  : 25 october 2026

Run it:   python template.py


"""

# ====================================================================== CLASS


class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Stores the label, value and limit for each record."""
        self.label = label
        self.value = value 
        self.limit = limit

    def status(self):
        """Checks if the record is over the limit."""
        percent = (self.value / self.limit) *100

        if percent >= 100:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS



def load_records(path):
    """Reads the file and stores the records in a list."""
    records = []

    with open(path) as f:
        for line in f :
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))

    return records 

records = load_records("Week 05 - Classes and Objects/LAB/my_records.txt")

# ==================================================================== OUTPUT

over_limit_count = 0 
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here
    print("source IP:", record.label)
    print("failed logins:", record.value)
    print("Total attempts:", record.limit)
    print("status:", record.status())
    
    if record.status() == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)
print("Total records over limit:", over_limit_count)


# ==========================================================================

