# S = list(input())
# def judge ():
#     judge = True
#     for i in range(1,1+len(S)):
#         if i%2==0 and (S[i-1]=="L" or  S[i-1]=="U" or S[i-1]=="D"):
#             continue
#         elif i%2==1 and (S[i-1]=="R" or  S[i-1]=="U" or S[i-1]=="D"):
#             continue
#         else:
#             judge = False
#             break
#     if (judge):
#         return "Yes"
#     else:
#         return "No"

# print(judge())

# S = str(input())
# odd = "RUD"
# even = "LUD"
# frag = True

# for i in range(len(S)):
#     if i%2 == 0 and S[i] not in odd:
#         frag =False
#         break
#     if i%2 != 1 and S[i] not in even:
#         frag = False
#         break
# if frag:
#     print("Yes")
# else:
#     print("No")

s = list(input())
odd = s[::2]
even = s[1::2]
ans = "Yes"
if "L" in odd or "R" in even:
    ans = "No"
print(ans)