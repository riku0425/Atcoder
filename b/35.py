s = input()
if s != s[::-1]:
    print("No")
    exit()

front = s[:int((len(s)-1)/2)]
back = s[int((len(s)-1)/2)+1:]
if front != front[::-1]:
    print("No")
    exit()
if back != back[::-1]:
    print("No")
    exit()
print("Yes")