N = int(input())
a = []
for _ in range(N):
    a.append(input())
AC = str(a.count("AC"))
WA = str(a.count("WA"))
TLE = str(a.count("TLE"))
RE = str(a.count("RE"))
print("AC x "+AC)
print("WA x "+WA)
print("TLE x "+TLE)
print("RE x "+RE)