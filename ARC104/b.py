N, S = input().split()
S_list = list(S)
cnt = 0
moji4 = ["ATAT","TATA","ATTA","TAAT","CGCG","GCGC","CGGC","GCCG",
        "ATCG","ATGC","TACG","TAGC","TCGA","TCAG","CTGA","CTAG","AGCT","TGCA"]
for i in range(int(N)-1):
    moji_2 = "".join(S_list[i:i+2])
    moji_4 = "".join(S_list[i:i+4])
    moji__4 = "".join(S_list[i-2:i+2])
    if moji_2=="AT" or moji_2=="TA" or  moji_2=="CG" or moji_2=="GC":
        cnt += 1
        if (((moji_4 or moji__4) in moji4) or (len(set(S_list[i-2:i+2]))==4 or len(set(S_list[i:i+4]))==4)):
            cnt +=1
    else:
        if (((moji_4 or moji__4) in moji4) or (len(set(S_list[i-2:i+2]))==4 or len(set(S_list[i:i+4]))==4)):
            cnt +=1
       
    

print(cnt)