"""
RECORD CHECK  -  my version
===========================

Name  :Siddiqah 
Lane  : Cyber  
Date  :25/09/2026

Run it:   python template.py


"""

# ==================================================================== INPUT


label = input("Enter source IP:")
first = float(input("enter failed logins :"))
second = float(input("enter total attempts :"))


# ================================================================== PROCESS


difference = second - first 
percent = (first / second) * 100
successful_attempts = second - first


# =================================================================== OUTPUT

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

