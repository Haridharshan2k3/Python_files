# input="b4a1d3"
# output=abd134
s=input("enter the string:")
s1=s2=s3=""
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    s3=s3+x
for x in sorted(s2):
    s3=s3+x
print(s3)