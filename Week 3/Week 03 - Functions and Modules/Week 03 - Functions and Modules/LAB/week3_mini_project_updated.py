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

# checks the percentage and return the status
def status_of(percent):
    # checks if the percentage is 100 or more 
    if percent >= 100 :
        return "OVER LIMIT"
    # checks if the percenatge is 100 or more 
    elif percent >= 90 :
        return "WARNING"
    # returns ok if the percentage is below 90
    else :
        return "OK"
# calculates the difference and percenatage 
def check (value , limit):
    # subtract the limit from the value 
    difference = limit - value
    # calculates the percentage 
    percent = (value /limit)* 100
    #returns both calculated values 
    return difference , percent
# displays the record report 
def print_report (label,value,limit,difference,percent,status):
    # prints the heading and record name 
    print ("=" * 34)
    print (f"RECORD CHECK-{label}")
    print ("=" * 34)
    print(f"value         :{value:>10.2f}")
    print (f"limit         :{limit:10.2f}")
    print (f"difference     :{difference:10.2f}")
    print (f"percent         :{percent:10.2f}%")
    print (f"status           :{status:>10}")
    print ("=" * 34)
# asks the user to enter in there source IP 
label = input("Enter source IP:")
# gets the number of failed loggins 
value= float(input("enter failed logins :"))
# gets the total number of attempts 
limit = float(input("enter total attempts :"))


# ================================================================== PROCESS
# calculates the difference and percentage using the check function 
difference , percent = check(value, limit)
# checks the percenatge and gets the status 
status = status_of(percent)

# =================================================================== OUTPUT
# print the record heading and source IP 
# shows the value and limit 
# shows the difference, percentage and status
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
# starts the count at 0 
over_count = 0 
# adds 1 if the status is over the limit 
if status == "OVER LIMIT":
    over_count += 1
# keeps asking for records until the user types quit 
while True:
    label = input("enter source ip (or quit):")
# stops the loop when the user enters quit 
    if label =="quit":
        break 
# gets the failed logins and total attempts 
    value= float(input("enter failed logins:"))
    limit=float(input("enter total attemps:"))
 # calculates the difference and percenatge    
    difference, percent=check(value,limit)
 # checks the ststus of the record 
    status = status_of(percent)
        
    print_report(label, value , limit , difference , percent ,status)
# shows the total number of reords over the limit 
print(f"total records over limit:{over_count}")






# ==========================================================================
