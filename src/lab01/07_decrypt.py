code=input()
orig=''
main=None
digit=None
second=None
for i in range(len(code)):
    if code[i].isupper() and main is None:
        main=i
    if code[i].isdigit() and digit is None and main is not None:
        digit=i
        second=i+1
step=second-main
i=main
while i<len(code):
    orig+=code[i]
    if code[i]=='.':
        break
    i+=step
print(orig)

    