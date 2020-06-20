a_hrs = int(input())
b_hrs = int(input())
h_hrs = int(input())

if a_hrs > h_hrs:
    print("Deficiency")
elif b_hrs < h_hrs:
    print("Excess")
else:
    print("Normal")
