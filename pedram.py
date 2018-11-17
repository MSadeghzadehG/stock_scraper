import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Bank.of.M.E..csv')
print(df.head())
l = list(df['<CLOSE>'])
mins = []
maxs = []
for i in range(1,len(l)-1):
    ch1 = 0
    ch2 = 0
    if l[i]>=l[i-1] and l[i]>=l[i+1]:
        maxs.append(i)
        ch2 = 1 
    elif l[i]<=l[i-1] and l[i]<=l[i+1]:
        mins.append(i)
        ch1 = 1
# print(mins)
plt.plot([i for i in range(0,len(l))],[l[i] for i in range(0,len(l))],color='blue')
# plt.scatter(mins,[l[i] for i in mins],color='green')

mins1 = [[mins[0]]]
first = mins[0]
num=0
for i in range(1,len(mins)):
    ch = False
    for j in range(first,len(l)):
        # print(str(j) + ' ' +str(i) + ' ' +str(mins[i]) + ' ' +str(l[first]+(j-first)*(l[mins[i]]-l[first])/(mins[i]-first)) + ' ' +str(l[j]))
        if l[j]<l[first]+(j-first)*(l[mins[i]]-l[first])/(mins[i]-first):
            ch = True
            break
    if ch:
        # print('omad')
        mins1[num].append(mins[i-1])
        first=mins[i]
        num+=1
        mins1.append([mins[i]])

for m in mins1:
    plt.plot(m,[l[i] for i in m],color='red')

maxs1 = [[maxs[0]]]
first = maxs[0]
num=0
for i in range(1,len(maxs)):
    ch = False
    for j in range(first,len(l)):
        # print(str(j) + ' ' +str(i) + ' ' +str(mins[i]) + ' ' +str(l[first]+(j-first)*(l[mins[i]]-l[first])/(mins[i]-first)) + ' ' +str(l[j]))
        if l[j]>l[first]+(j-first)*(l[maxs[i]]-l[first])/(maxs[i]-first):
            ch = True
            break
    if ch:
        # print('omad')
        maxs1[num].append(maxs[i-1])
        first=maxs[i]
        num+=1
        maxs1.append([maxs[i]])

for m in maxs1:
    plt.plot(m,[l[i] for i in m],color='red')


plt.show()
# plt.plot(mins,[l[i] for i in mins],'red')

# print(mins1)
