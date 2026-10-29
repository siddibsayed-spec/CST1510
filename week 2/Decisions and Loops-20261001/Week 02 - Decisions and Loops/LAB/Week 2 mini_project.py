"""
RECORD CHECK  -  my version
===========================

Name  :Siddiqah 
Lane  :  IT  
Date  : 02/10/2025

Run it:   python template.py


"""

# ==================================================================== INPUT


label = input ("Enter your host name :")
value = float (input("Enter GB used :"))
limit = float (input("Enter GB total :"))   


# ================================================================== PROCESS


difference = limit - value 
percent = (value /limit ) *100

if percent >= 100:
    status = ("OVER LIMIT")

elif percent >= 90 :
    status =("WARNING")

else :
    status =("OK")


# =================================================================== OUTPUT


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

