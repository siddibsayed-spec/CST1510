"""
RECORD CHECK  -  my version
===========================

Name  :siddiqah sayed 
Lane  :   Cyber
Date  : 17 october 2026

Run it:   python template.py


"""

# =================================================================== FUNCTIONS


def check_record(value, limit):
    """
Checks if the value is over the limit.
it calculates the difference and percentage thenit prints out the results and status.
"""
# calculates the difference and percentage 
    difference = value - limit 
    percent = value / limit *100 
# checks the percentage and sets the status
    if percent >= 100 :
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference , percent , status 

def print_report(label,value,limit,difference,percent,status):
    """
Shows each record in detail such as the  value, limit and difference and it Shows the percentage and status.
"""
# shows the total records over the limit 
    if status == "Total":
        print("Total records Over Limit:", value)
        return
 
    if status == "Error":
        print(label)
        return
 
 # prints the records details 
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"value         :{value:>10.2f}")
    print(f"limit         :{limit:>10.2f}")
    print(f"difference    :{difference:>10.2f}")
    print(f"percent       : {percent:>10.2f}%")
    print(f"status        : {status:>10}")
    print("=" * 34)



# ====================================================================== STORE


# opens the file and loads the records 
def load_records(path):
    """
Opens the file and reads the records then it Saves each record in a dictionary and it Gives back a list of all the records.
"""
# creates an empty list to store the records 
    records = []   
 # opens the file and reads each line    
    with open (path ,"r") as f:
        for line in f :
            label,value,limit = line.strip().split(",")
# saves each record in the list 
            records.append({
                "label" : label, 
                "value" : float(value),
                "limit" :float(limit),
             })
    return records 
# tries to load the records from the file 
try:
    records = load_records("records.txt")
 # shows an error if the file is not found 
except FileNotFoundError:
    records = []
    print_report("File is not found","","","","","Error")
 

records = load_records(r"C:\Users\aboos\Documents\CST1510\week 4\Week 04 - Lists, Dictionaries and Files\LAB\my_records.txt")




# =============================================================== PROCESS + OUTPUT

# starts counting records over the limit 
over_count = 0 
# opens the results file to save the records 
with open ("results.txt" , "w") as f :
 # goes through each record in the list    
    for record in records :
        print(record["label"])
        difference , percent , status = check_record(
            record["value"], record ["limit"]
        )
# displays the report for each record 
        print_report(
            record["label"], record["value"], record["limit"],
            difference , percent,status
        )
# adds 1 if the record is over the limit 
        f.write(f"{record['label']},{status}\n")
        if status == "OVER LIMIT":
            over_count += 1
# shows the total number of records over the limit 
print (f"total records OVER LIMIT :{over_count}")


# ==========================================================================

