"""
RECORD CHECK  -  my version
===========================

Name  :siddiqah sayed 
Lane  : Cyber 
Date  :10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    if percent >= 100 :
        return "OVER LIMIT"
    elif percent >= 90 :
        return "WARNING"
    else :
        return "OK"

def check (value , limit):
    difference = value - limit 
    percent = (value /limit)* 100
    return difference , percent

def print_report (label,value,limit,difference,percent,status):
    print ("=" * 34)
    print (f"RECORD CHECK-{label}")
    print ("=" * 34)
    print(f"value         :{value:>10.2f}")
    print (f"limit         :{limit:10.2f}")
    print (f"difference     :{difference:10.2f}")
    print (f"percent         :{percent:10.2f}%")
    print (f"status           :{status:>10}")
    print ("=" * 34)






label = input("Enter source IP:")
value= float(input("enter failed logins :"))
limit = float(input("enter total attempts :"))


# ================================================================== PROCESS



difference , percent = check(value, limit)
status = status_of(percent)

# =================================================================== OUTPUT




print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"value         :{value:>10.2f}")
print(f"limit         :{limit:>10.2f}")
print(f"difference    :{difference:>10.2f}")
print(f"percent       : {percent:>10.2f}%")
print(f"status        : {status:>10}")
print("=" * 34)

over_count = 0 

while True:
    label = input("enter source ip (or quit):")

    if label =="quit":
        break 

    value= float(input("enter failed logins:"))
    limit=float(input("enter total attemps:"))
    
    difference, percent=check(value,limit)
    status = status_of(percent)
    
    if status =="OVER LIMIT":
        over_count += 1 
        
    print_report(label, value , limit , difference , percent ,status)

print(f"total records over limit:{over_count}")






# ==========================================================================
