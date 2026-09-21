p_count=int(input("in_1:"))
och=0
zaoch=0
for i in range(p_count):
    line=input(f"in_{i+2}:")
    part_line=line.split()
    time=part_line[3]
    if time=='True':
        och+=1
    elif time=='False':
        zaoch+=1
print("out:",och,zaoch)