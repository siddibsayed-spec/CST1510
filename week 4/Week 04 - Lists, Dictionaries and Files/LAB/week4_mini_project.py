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
    difference = value - limit 
    percent = value / limit *100 

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

    if status == "Total":
        print("Total records Over Limit:", value)
        return
 
    if status == "Error":
        print(label)
        return
 
 
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


# replace with your code
def load_records(path):
    """
Opens the file and reads the records then it Saves each record in a dictionary and it Gives back a list of all the records.
"""
    records = []   
    
    with open (path ,"r") as f:
        for line in f :
            label,value,limit = line.strip().split(",")

            records.append({
                "label" : label, 
                "value" : float(value),
                "limit" :float(limit),
             })
    return records 

try:
    records = load_records("records.txt")
 
except FileNotFoundError:
    records = []
    print_report("File is not found","","","","","Error")
 

records = load_records(r"C:\Users\aboos\Documents\CST1510\week 4\Week 04 - Lists, Dictionaries and Files\LAB\my_records.txt")




# =============================================================== PROCESS + OUTPUT


over_count = 0 
with open ("results.txt" , "w") as f :
    for record in records :
        print(record["label"])
        difference , percent , status = check_record(
            record["value"], record ["limit"]
        )

        print_report(
            record["label"], record["value"], record["limit"],
            difference , percent,status
        )

        f.write(f"{record['label']},{status}\n")
        if status == "OVER LIMIT":
            over_count += 1

print (f"total records OVER LIMIT :{over_count}")


# ==========================================================================

