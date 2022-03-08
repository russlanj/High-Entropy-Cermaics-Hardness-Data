## Written by: Russlan Jaafreh & Kang Yoo-Seong

df_B2 = pd.read_excel('HCP_high_hardness_C.xlsx',engine='openpyxl') ## output file from last code "Crystal structure filtering code.py"


from pymatgen.core import periodic_table as pt
import statistics

rad = 0
sum_rad = []
average_rad = []
less_than_list = []
all_list = []
cnt = 0
name=''
for k in df_B2:
    name=''
    comp = pg.Composition(k)
    if 0 == 0:
        for j in comp:
            if 'Ce' == str(j):
                radCe = 1.85
                sum_rad.append(radCe)
                name = name + 'Ce' + '0.2'
            elif 'La' == str(j):
                radLa = 1.95
                sum_rad.append(radLa)
                name = name + 'La' + '0.2'
            else:
                rad = pg.Element(j).atomic_radius_calculated
                sum_rad.append(rad)
                name = name + str(j) + '0.2'
        average_rad.append([name,statistics.mean(sum_rad)])


less_than_list = []
for l in average_rad:
    comp = pg.Composition(l[0])
    less_list = []
    for m in comp:
        if 'Ce' in str(m):
            rad_m = 1.85
            less_list.append(rad_m)
        elif 'La' in str(m):
            rad_m = 1.95
            less_list.append(rad_m)
        else:
            rad_m = pg.Element(m).atomic_radius_calculated
            less_list.append(rad_m)
    
    less_than_list.append([l[0],less_list,l[1]])
    
cnt = cnt + 1

new_list = []
pre = []
import math
for k in less_than_list:
    pre_ = 0
    for w in k[1]:
        pre_ = 0.2*((1-w/k[2])**2)
        sum_pre = pre_ + pre_
    pre.append([k[0] + "C",math.sqrt(sum_pre)])

less_fif = []
for b in pre:
    if b[1] > 0.06:
        continue
    if b[1] < 0.06:
        less_fif.append(b)

df_less_than_006 = pd.DataFrame(less_fif,columns = ['filename','sigma'])
df_all= pd.DataFrame(pre,columns = ['filename','sigma'])
df_less_than_006.to_excel("less_than006_C.xlsx")  
df_all.to_excel("all_radius006_C.xlsx") 

