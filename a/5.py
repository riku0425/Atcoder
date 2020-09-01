a,b,c= map(int, input().split()) #i_1 i_2を取得し、iに値を入れる
print(min(a+b,b+c,c+a))