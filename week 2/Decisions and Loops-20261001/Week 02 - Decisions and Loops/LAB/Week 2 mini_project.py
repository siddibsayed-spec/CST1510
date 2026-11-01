"""
RECORD CHECK  -  my version
===========================

Name  :Siddiqah 
Lane  :  IT  
Date  : 02/10/2025

Run it:   python template.py


"""

# ==================================================================== INPUT

# ask the user to enter in their hostname
label = input ("Enter your host name :")
# gets the amount of GB used 
value = float (input("Enter GB used :"))
# the total GB available 
limit = float (input("Enter GB total :"))   


# ================================================================== PROCESS

# calculate how much storage is left
difference = limit - value 
# calculates the percentage of storage used
percent = (value /limit ) *100
# checks if the percentage is at or over the limit 
if percent >= 100:
    status = ("OVER LIMIT")
# check if the storage is at 90% or more 
elif percent >= 90 :
    status =("WARNING")
# show ok if storage is below 90%
else :
    status =("OK")


# =================================================================== OUTPUT

# prints the record heading with the host name 
# shows the used and total storage 
# shows the remianing storage and percent used 
# shows the storage status 
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" used  :{value:>10.2F}")
print(f" total :{limit:>10.2f}")
print(f" difference  :{difference:>10.2f}")
print(f" percent  :{percent:>10.2f}%")
print(f" status :{status:>10}")

print("=" * 34)


# ==========================================================================

