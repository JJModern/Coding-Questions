import sys

f = sys.stdin.read().splitlines()


result = set(["keys", "phone", "wallet"])  - set(f[1:])

if len(result) == 0:
    print("ready")
else:
    for item in sorted(list(result)):
        print(item)