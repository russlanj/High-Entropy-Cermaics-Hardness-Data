## Written by: Russlan Jaafreh & Kang Yoo-Seong

#initializing the crystal struture of elements
hcp = ['Be','Mg','Sc','Y','Lu','Ti','Zr','Hf','Tc','Re','Ru','Os','Co','Zn','Cd','Tl','Gd','Tb','Dy','Ho','Er','Tm','Pm','Nd','Pr','Ce','La','In','Sn','Ta']
fcc = ['Ni','Cu','Rh','Pd','Pt','Ir','Au','Ag','Al','Pb','Ca','Sr','Ce']
bcc = ['v','Nb','Ta','W','Mo','Cr','Mn','Fe','Eu','Ba']
tetr = []
rho = ['Hg','Bi','Sb','As','Sm']
a = set(hcp)
b = set(fcc)
c = set(bcc)
d = set(tetr)
e = set(rho)

hcp_set = a.intersection(metallic_set)
fcc_set = b.intersection(metallic_set)
bcc_set = c.intersection(metallic_set)
tetr_set = d.intersection(metallic_set)
rho_set = e.intersection(metallic_set)

#reading the highest hardness of eah HECs
df_composition = pd.read_csv('highest_hardness_C.csv') ##please import the highest hardness (>40 as highest_hardness_C or _B or BC etc)
filtered_comp = [] 
for i in df_composition['filename']:
    i1 = i.replace("0.2","")
    i2 = i1[:-1]
    #i2 = i1.replace("BC",'') # for BC
    filtered_comp.append(i2)
df_composition['filtered'] = filtered_comp

# to find the highest hardness in a single crystal structure for the 4 metals
index_list = []
cnt = 0
for i in df_composition['filtered']:
    elemcomp = pg.Composition(i).elements
    switches = 0
    for j in elemcomp:
        if not str(j) in hcp_set:
            switches = 1
            #print(cnt,elemcomp,j)
            break
    if switches == 0:
        print(switches)
        index_list.append(cnt)
        switches = 0
    cnt = cnt + 1

df_hcp = pd.DataFrame()
temp = []
for count, item in enumerate(df_composition.loc[index_list].iterrows()):
    temp.append(list(item[1]))
        
df_composition.loc[index_list]
df_hcp = pd.DataFrame(temp, columns=['filename','hardness','load','filtered'])
df_hcp.to_excel("HCP_high_hardness_C.xlsx")  ## save the high hardness hcp, fcc, bcc HECs