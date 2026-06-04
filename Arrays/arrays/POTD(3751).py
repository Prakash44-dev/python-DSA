# ran = [120, 122]
# digits =[]
# temp= 0
# wavy = 0
# count =0
# # for i in range(ran[0],ran[1]+1):
# temp = 120
# while temp!=0:
#     digits.append(temp%10)
#     temp = temp//10
# if len(digits)<3  :
#     wavy=0
#     exit()
# for j in range(len(digits)) :
#     if digits[j]<


# print(digits)


ran  = [4848,4848]
wavy = 0
for i in range(ran[0], ran[1]+1) :
    s = str(i)
    if len(s)<3:
        continue
    for j in range (1,len(s)-1):
        if s[j]>s[j-1] and s[j]>s[j+1] :
            wavy+=1
        elif s[j]<s[j-1] and s[j]< s[j+1]:
            wavy+=1   
print(wavy)            
