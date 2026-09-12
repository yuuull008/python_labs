p_count=int(input())
och=0
zaoch=0
for i in range(p_count):
    line=input()
    part_line=line.split()
    time=part_line[3]
    if time=='True':
        och+=1
    elif time=='False':
        zaoch+=1
print(och,zaoch)