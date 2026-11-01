"""
RECORD CHECK  -  my version
===========================

Name  :siddiqah sayed 
Lane  : Cyber 
Date  : 25 october 2026

Run it:   python template.py


"""

# ====================================================================== CLASS

# creates a class to store record information 
class Record:
 # starts the over limit count at 0    
    over_limit_count = 0
# sets up the details for each record
    def __init__(self, label, value, limit):
        """Stores the label, value and limit for each record."""
  # store the label, value, limit      
        self.label = label
        self.value = value 
        self.limit = limit
# checks the status of the record 
    def status(self):
        """Checks if the record is over the limit."""
        percent = (self.value / self.limit) *100
# checks if the percentage is 100 or more 
# adds 1 to the over limit count 
        if percent >= 100:
            Record.over_limit_count += 1
            return "OVER LIMIT"
 # shows a warning if the percentage is at 90 or more        
        elif percent >= 90:
            return "WARNING"
 # returns ok if percentage is below 90       
        else:
            return "OK"


# ==================================================================== RECORDS



def load_records(path):
    """Reads the file and stores the records in a list."""
 # creates an emty list to store the records    
    records = []
# opens the file and read each line 
    with open(path) as f:
        for line in f :
 # splits each line into label, value and limit            
            label, value, limit = line.strip().split(",")
        # creates a record object and adds it to the list     
            records.append(Record(label, float(value), float(limit)))
# return all the records 
    return records 
# loads the records from the text file 
records = load_records("Week 05 - Classes and Objects/LAB/my_records.txt")

# ==================================================================== OUTPUT
# start counting the records over the limit 
over_limit_count = 0 
# goes through each record in the list 
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # displays the records details 
    print("source IP:", record.label)
    print("failed logins:", record.value)
    print("Total attempts:", record.limit)
    print("status:", record.status())
 # checks if the record is over the limit    
    if record.status() == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)
 # shows the total records over the limit    
print("Total records over limit:", over_limit_count)


# ==========================================================================

