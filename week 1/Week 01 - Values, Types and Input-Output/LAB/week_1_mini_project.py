"""
RECORD CHECK  -  my version
===========================

Name  :Siddiqah 
Lane  : Cyber  
Date  :25/09/2026

Run it:   python template.py


"""

# ==================================================================== INPUT

# asks the user to enter their source IP 
label = input("Enter source IP:")
# gets the number of failed logins 
first = float(input("enter failed logins :"))
# gets the total number of attemps 
second = float(input("enter total attempts :"))


# ================================================================== PROCESS

# calculates the difference between attempts and failed logins 
difference = second - first 
# calculates the percent of failed loggins 
percent = (first / second) * 100
# calculates the sucessfull login attempts 
successful_attempts = second - first


# =================================================================== OUTPUT
# prints the record heading with the source IP neatly formated 
# shows the failed logins and total attempts 
# shows the difference and percentage 
# shows the number of sucesfull attempts 
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" failed  :{first:>10.2F}")
print(f" attempts:{second:>10.2f}")
print(f" difference:{difference:>+10.2f}")
print(f" percent  :{percent:>10.2f}%")
print(f" successful:{successful_attempts:>10.2f}")

print("=" * 34)


# ==========================================================================

