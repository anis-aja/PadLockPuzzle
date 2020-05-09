#there is a lock with key number. Guess which number is the key number with below condition

c1=[1,4,7]    # 1 digit is right but in the wrong place
c2=[1,8,9]    # 1 digit is right and in its right place
c3=[9,6,4]    # 2 digit is right but in wrong place
c4=[5,2,3]    # all digits are wrong
c5=[2,8,6]    # 1 digit is right but in the wrong place

c1_=c1.copy()
c2_=c2.copy()
c3_=c3.copy()
c5_=c5.copy()

cresult=[]

for forbidNum in c4:    #delete all number in c4
    if forbidNum in c1: c1_.remove(forbidNum)
    if forbidNum in c2: c2_.remove(forbidNum)
    if forbidNum in c3: c3_.remove(forbidNum)
    if forbidNum in c5: c5_.remove(forbidNum)
 
            
del c4

for ii in range(2):    #delete number with right and wrong in same place
    dele=False
    if c2[ii]==c1[ii]:
        c1_.remove(c1[ii])
        dele=True
    if c2[ii]==c3[ii]:
        c3_.remove(c3[ii])
        dele=True
    if c2[ii]==c5[ii]:
        c5_.remove(c5[ii])
        dele=True
    if dele==True: c2_.remove(c2[ii])


#get index    
if len(c2_) == 1:       #right number right position
    c2index=c2.index(c2_[0])
    c2result=c2_[0]
if len(c5_)==1 :        #right number wrong position
    c5result = c5_[0]    
  #  c5index=c5.index(c5_[0])

    if c5result in c3:
        indexfail=c3.index(c5result)
        for ii in range (3):
            if ii != indexfail and ii!= c2index:
                c5index=ii
                break
            
    
print (c1_, c2_, c3_, c5_)
print(c1, c2, c3, c5)
print("------")


#find one wrong number in c3
if c2result in c3_: c3_.remove(c2result)
if c5result in c3_: c3_.remove(c5result)
if len(c3_) == 1:
    if c3_[0] in c1_: c1_.remove(c3_[0])

if len(c1_)==1:
    c1result = c1_[0]
 #   c1index=c1.index(c1_[0])
    for ii in range(3):
        if ii!= c5index and ii!= c2index:
            c1index=ii
            break
    
    
print (c1_, c2_, c3_, c5_)
print(c1, c2, c3, c5)
print("------")


print(c1index, c2index, c5index)
print(c1result, c2result, c5result)

for ii in range (3):
    if ii == c1index:
        cresult.append(c1result)
        continue
    if ii == c2index:
        cresult.append(c2result)
        continue
    if ii == c5index:
        cresult.append(c5result)
        continue

print (cresult)

