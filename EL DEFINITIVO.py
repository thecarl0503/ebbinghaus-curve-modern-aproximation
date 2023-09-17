from ast import While
from copyreg import remove_extension
from csv import list_dialects
from datetime import datetime
from datetime import timedelta  
from operator import itemgetter
from datetime import date
from pickle import TRUE
from re import X
from telnetlib import XAUTH
from timeit import repeat
from tkinter import DISABLED, S
from collections import defaultdict
import math as ma
import collections, functools, operator
from itertools import chain

#1. DATOS:
    #1.1. 
fechas_de_examenes={
    "F":datetime(2022,10,18), 
    "C":datetime(2022,10,25),
    "E":datetime(2022,10,12),
    "L":datetime(2022,12,6)}
#1.2. Espacios en semana (1)Lunes...(7)Domingo. En minutos [clase, mañana, tarde, en el minibus]
espacios_en_semana={1:[150,100,150,100], 2:[400,50,0,100], 3:[0,200,400,0], 4:[150,100,200,100], 5:[0,200,400,0], 6:[0,200,100,0], 7:[0,200,200,0]}
clases_en_semana={1:("E"), 2:("F", "L"), 3:(), 4:("F"), 5:(), 6:(), 7:()}
tiempos_enteros_teoricos={1:150, 2:100, 3:50, 4:25}
tiempos_cuartos_teoricos={1:40, 2:36, 3:32, 4:28}
tiempos_cuartos_practicos={1:100, 2:100, 3:100, 4:50}
a_fisica=["Zemanky", "Resnick&Krane","Feynman"]
a_calculo=[ "Dennis Zill", "Stewart"]
a_laboratorio=["Youtube","Purcell"]
a_estadistica=["Moya","Marian"]
masters={"F":a_fisica,"C":a_calculo,"L":a_laboratorio,"E":a_estadistica}
fechas_de_clase_fisica={

"F1":0, "F2":0, 
"F3":0, "F4":0, 
"F5":datetime(2022,9, 20), "F6":datetime(2022,9, 22),  
"F7":datetime(2022,10, 4), "F8":datetime(2022,10, 6)}

fechas_de_clase_calculo={
"C1":datetime(2022,9,5), "C2":datetime(2022,9,5), 
"C3":datetime(2022,9,5), "C4":datetime(2022,9,5), 
"C5":datetime(2022,9,5), "C6":datetime(2022,9,5), 
"C7":datetime(2022,9,5), "C8":datetime(2022,9,5)}
#execcion de rango para clase 2 de laboratorio
fechas_de_clase_laboratorio={
"L1":datetime(2022,10, 11), "L2":datetime(2022,10, 18), 
"L3":datetime(2022,10, 25), "L4":datetime(2022,11, 8), 
"L5":datetime(2022,11, 15),"L6":datetime(2022,11, 22)}

fechas_de_clase_estadistica={
"E1":datetime(2022,9,19), "E2":0, 
"E3":0, "E4":0,
"E5":0, "E6":0, 
"E7":0, "E8":datetime(2022,10,10)}

limites_teoricos=[0.95,0.8,0.7,0.62]
limites_practicos=[0.95, 0.85, 0.7, 0.5]
limites={"T":limites_teoricos,"P":limites_practicos}

#3.FUNCIONES
    #FUNCIONES DE TEORIA
def T1a(x):
    return 0.894*x**-0.269
def T2a(x):
    return 0.774*x**-0.305
def T1b(x):
    return 0.774*x**-0.305
def T2b(x):
    return 0.779*x**-0.327
def T1c(x):
    return 0.779*x**-0.327
def T2c(x):
    return 0.742*x**-0.389
def T3a (x):
    return 0.717*x**-0.365
def T3b (x):
    return 0.717*x**-0.365
def T4a (x):
    return 0.674*x**-0.427
def T4b (x):
    return 0.674*x**-0.427
def T3c (x):
    return 0.669*x**-0.384
def T4c (x):
    return 0.538*x**-0.371
def T3d (x):
    return 0.484*x**-0.311
def T4d (x):
    return 0.423*x**-0.302

    #FUNCIONES DE PRACTICA
# ------------------------Falta cambiar funciones
def P1a(x):
    return 0.894*x**-0.269
def P2a(x):
    return 0.774*x**-0.305
def P1b(x):
    return 0.774*x**-0.305
def P2b(x):
    return 0.779*x**-0.327
def P1c(x):
    return 0.779*x**-0.327
def P2c(x):
    return 0.742*x**-0.389
def P3b (x):
    return 0.717*x**-0.365
def P3c (x):
    return 0.717*x**-0.365
def P4b (x):
    return 0.674*x**-0.427
def P4c (x):
    return 0.674*x**-0.427
def P4d (x):
    return 0.669*x**-0.384
def P3d (x):
    return 0.538*x**-0.371
#ESTABLECEMOS UNA FUNCION DE SUMA LIMITE
def lim(x,y):
    if x>y:
        return y
    else:
        return x
def tau (x,y):
        if x<=0:
            return 0
        else:
            ggg=0.374 + 0.268 *ma.log((x/len(y))*10)
            if ggg>1:
                return 1
            elif ggg<0:
                ggg=0
            else:
                return ggg
def pau (x,y):  
    if x<=0:
        return 0
    else:
        ggg= 0.145 + 0.0767*(x*10/len(y)) + (1.25*(10)**-3)*(x*10/len(y))**2
        if ggg>1:
            return 1
        elif ggg<0:
            ggg=0
        else:
            return ggg


cl_de_materias={

"FT1":0, "FT2":0, "FT3":0, "FT4":0, 
"FT5":0, "FT6":0,  "FT7":0, "FT8":0,

"CT1":0, "CT2":0, "CT3":0, "CT4":0, 
"CT5":0, "CT6":0, "CT7":0, "CT8":0,

"ET1":0, "ET2":0, "ET3":0, "ET4":0, 
"ET5":0, "ET6":0, "ET7":0, "ET8":0,

"FP1":0, "FP2":0, "FP3":0, "FP4":0, 
"FP5":0, "FP6":0, "FP7":0, "FP8":0,

"CP1":0, "CP2":0, "CP3":0, "CP4":0, 
"CP5":0, "CP6":0, "CP7":0, "CP8":0,

"EP1":0, "EP2":0, "EP3":0, "EP4":0, 
"EP5":0, "EP6":0, "EP7":0, "EP8":0
}

diferencias={}
for j in fechas_de_examenes:
    diferencias[j]=((((fechas_de_examenes[j])-(datetime.now()))).days)
fechas_ordenadas=(sorted(diferencias.items(), key =itemgetter(1), reverse=True))

dias_y_espacios_disponibles={}
def genera_rango_fechas (fecha_1, fecha_2):
    fechas=[]
    dias=(fecha_2-fecha_1).days
    for i in range(dias):
        fechas.append(fecha_1+timedelta(i))
    return fechas
inicio = datetime.now()
fin =fechas_de_examenes[str(((fechas_ordenadas[0]))[0])]
rango_de_fechas=genera_rango_fechas(inicio, fin)
#print(rango_de_fechas)
for i in rango_de_fechas:
    dias_y_espacios_disponibles[(i.date())]=[len(clases_en_semana[i.isoweekday()]),(espacios_en_semana[i.isoweekday()])[1],(espacios_en_semana[i.isoweekday()])[2],(espacios_en_semana[i.isoweekday()])[3]]

def concatenar (lista):
    fechas={}
    for d in lista:
        fechas.update(d)
    return fechas
fechas=[fechas_de_clase_fisica,fechas_de_clase_calculo, fechas_de_clase_estadistica, fechas_de_clase_laboratorio]
dic_fechas= concatenar(fechas)
agenda={}
for af in rango_de_fechas:
    agenda[af.date()]=[]
contador_bruto={}

for quien in cl_de_materias:
    contador_bruto[quien]={}


print(contador_bruto)

for yu in range(1):
    #ORDENAMOS POR FECHAS
    contador=contador_bruto.copy()
    for t in contador.items():
        p={}
        contador[t[0]]=p
        a=sorted(t[1])
        for n in a:
            p[n]=(t[1])[n]
    #ORDENAMOS LOS TIPOS Y ELEGIMOS EL MAYOR
    contador_solo_ordenado=contador.copy()
    for y in contador.items():
        r={}    
        for i in (y[1]).items():
            r[i[0]]=((sorted(i[1]))[0])
        contador[y[0]]=r   
    contador_fechas={}
    contador_tipos={}
    for s in contador.items():
        print("SSSSSSSSSSSSSSSS",s)
        if s[0][1]=="T":
            contador_fechas[s[0]]=list(s[1].keys())
            g=[]   
            for z in (s[1].values()):
                g.append(int(str(z)[0]))
            contador_tipos[s[0]]= g
    ranguitos_dic={}
    for i in contador_tipos.items(): 
        indices=[]
        a=("".join([str(_) for _ in i[1]])).count("1")
        if a>0:
            indice_lugar_de_1=(("".join([str(_) for _ in i[1]])).find("1")) 
            indices.append(indice_lugar_de_1)
            for l in range(0,a-1):
                ind_lugar1=(("".join([str(_) for _ in i[1]])).find("1",indices[-1]+1))
                indices.append(ind_lugar1)
        
        b=("".join([str(_) for _ in i[1]])).count("22")
        if b>0:
            indice_lugar_de_22=(("".join([str(_) for _ in i[1]])).find("22"))+1
            indices.append(indice_lugar_de_22)
            for m in range(0,b-1):
                ind_lugar22=(("".join([str(_) for _ in i[1]])).find("22",indices[-1]+1))
                #LE SUMO MÁS 1 PARA QUE ME DE EL INDICE DEL SEGUNDO.ESTA BIEN? creo que si :)
                indices.append(ind_lugar22+1)

        if -1 in indices:
            for k in range(0, indices.count(-1)):        
                indices.remove(-1)
        fechecitas=[]
        for u in indices:
            fechecitas.append((contador_fechas[i[0]][u]))
        (fechecitas.sort(reverse=True))
        if len(fechecitas)==0:
            fechecitas=[fechas_de_examenes[(str(i[0]))[0]]]+fechecitas+[datetime.now()-timedelta(days=30)]
        else:
            fechecitas=fechecitas+[datetime.now()-timedelta(days=30)]
        ranguitos=[]
        for t in range(0,len(fechecitas)-1):
            ranguitos.append([fechecitas[t],fechecitas[t+1]+timedelta(days=1)])
        for r in contador.keys():
            ranguitos_dic[f"{i[0][0]}{i[0][-1]}"]=ranguitos
    contador_en_ranguitos=contador_solo_ordenado.copy()

    for te in contador_solo_ordenado.items():
        b=[]
        for q in ranguitos_dic[f"{te[0][0]}{te[0][-1]}"]:
            a={}       
            for u in (list(te[1].keys())):
                if  q[0]>=u>=q[-1]:
                    #print()
                    a[u]=te[1][u]     
            b.append(a)
        contador_en_ranguitos[te[0]]=b
    for n in contador_en_ranguitos.items():
        contador_en_ranguitos[n[0]]=(list(n[1]))[::-1]
    for wa in contador_en_ranguitos.items():
        esa=wa[1].copy()
        for we in wa[1]:
            for wi in we.items():
                esalista=wi[1].copy()
                for wo in wi[1]:
                    if len(wo)<4:
                        rui=wa[1].index(we)
                        esalista[esalista.index(wo)]=f"{wo}-{len(masters[wa[0][0]])-wa[1][::-1].index(we)}"
                        we[wi[0]]=esalista
                        wa[1][rui]=we
    print("2222222222222222",contador_bruto)
    #print("CONTADOR EN RANGUITOS 1",contador_en_ranguitos)
    #print("CONTADOR BRTO 0",contador_bruto)
    for ia in contador_bruto.items():
        contador_bruto[ia[0]]=concatenar(contador_en_ranguitos[ia[0]])
    #print("CONTADOR BRUTO 2",contador_bruto)
    por_tipos_completo={}
    for pa in contador_en_ranguitos.items():
        hola=[]
        for pe in pa[1]:
            invertido=defaultdict(list)
            {invertido[tuple(v)].append(k) for k , v in pe.items()}
            resultado=dict(invertido)
            eso=[] 
            for pi in resultado.items():
                for po in pi[0]:
                    d=(po,pi[1])
                    
                    eso.append(d)
            dict3 = defaultdict(list)
            for k, v in eso:
                dict3[k].append(v[0])
            lira=dict(dict3)

            hola.append(lira)
        por_tipos_completo[pa[0]]=hola

    for ga in por_tipos_completo.items():
        for ge in ga[1]:
            geg={}
            for gi in ge.items():
                if ga[0][1]=="T":
                    if gi[0][0:2]=="1a":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T1a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="2a":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T2a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="1b":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T1b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="2b":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T2b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="1c":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T1c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="2c":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T2c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="3a":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T3a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="3b":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T3b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="4a":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T4a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="4b":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T4b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="3c":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T3c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="4c":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T4c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="3d":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T3d(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="4d":
                        l=[]
                        for go in gi[1]:                   
                            l.append(T4d(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                if ga[0][1]=="P":
                    if gi[0][0:2]=="1a":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P1a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="2a":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P2a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="1b":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P1b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="2b":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P2b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="1c":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P1c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="2c":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P2c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="3b":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P3b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="3c":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P3c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="4b":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P4b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="4c":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P4c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="4d":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P4d(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
                    if gi[0][0:2]=="3d":
                        l=[]
                        for go in gi[1]:                   
                            l.append(P3d(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                        ge[gi[0]]=sum(l)
    #print(por_tipos_completo)
    print("33333333333333333333",contador_bruto)
    for nea in por_tipos_completo.items():
        neo_lista=[]
        for nee in nea[1]:
            #print(nee)
            chi={}
            claves=[]
            for nei in nee.items():
                
                clave= f"{nei[0][0]}-{nei[0][-1]}"
                claves.append(clave)
            for neii in set(claves):
                lista_chi=[]
                for neo in nee.items():
                    if f"{neo[0][0]}-{neo[0][-1]}"==neii:
                        valor=neo[1]
                        lista_chi.append(valor)
                #print(neii, sum(lista_chi))
                #print("limite", limites[nea[0][1]][int(neii[0])-1])
                #print()
                
                chi[neii]=lim(sum(lista_chi),limites[nea[0][1]][int(neii[0])-1])
            neo_lista.append(chi)
        por_tipos_completo[nea[0]]=neo_lista
            
    #print(por_tipos_completo)

                #TIENES QUE COMPLETAR LA SUMA LIMITE CON EL ALGORITMO DE SUMA DE DICCIONARIOS, EXCEPTO QUE SUMATREMOS UNA LISTA DE CLAVES Y VALORES ASIGNADOS
                #completo
                #LUEGO PONERLE EL LIMITE A CADA SUMA
                #completo
                #REVISAR LOS PUNTOS A B Y C 
                #LUEGO COMPARAR LA PRUEBA 36 Y 37, 1 TIENEN QUE TENER RESULTADOS IGUALES Y CODIGOS IGUALES, 
                #print(clave,valor)
    print("33333333333333333333",contador_bruto)
    #print(por_tipos_completo)
    retenciones_gamma=por_tipos_completo.copy()  
    print("POR TIPOS COMPLETO1",por_tipos_completo)
    for ha in por_tipos_completo.items():
        if (ha[0][1])=="T":
            sumas=[]
            zumas=[]
            for he in ha[1]:
                ne=he.copy()
                #print("wwwww",he)
                for hi in he.items():
                    jj=tau(int(hi[0][-1]),masters[ha[0][0]])
                    ss=tau(int(hi[0][-1])-1,masters[ha[0][0]])
                    
                    he[hi[0]]=hi[1]*(jj-ss)
                    ne[hi[0]]=hi[1]*jj
                suma=sum(he[x] for x in he)
                zuma=sum(ne[y] for y in ne)
                sumas.append(suma)
                zumas.append(zuma)
            sumas2=[]
            zumas2=[]
            #print("SUMAS TEORICAS DELTA ",sumas)
            #print("SUMAS TEORICAS  X ",zumas)
            for rie in sumas:
                
                quie=tau(len(masters[ha[0][0]])-sumas[::-1].index(rie),masters[ha[0][0]])-tau(len(masters[ha[0][0]])-(sumas[::-1].index(rie)+1),masters[ha[0][0]])
                #print("RIE",rie,"LIMITE",quie)
                rie=lim(rie,quie)
                #print(quie)
                sumas2.append(rie)
            for rio in zumas:
                quio=tau(len(masters[ha[0][0]])-zumas[::-1].index(rio),masters[ha[0][0]])
                #print("RIO",rio,"LIMITE",quio)
                rio=lim(rio,quio)
                zumas2.append(rio)
            feo=sum(sumas2)
            fea=sum(zumas2)
            por_tipos_completo[ha[0]]=feo
            retenciones_gamma[ha[0]]=fea

        if ha[0][1]=="P":
            sumas=[]
            zumas=[]
            for he in ha[1]:
                ne=he.copy()
                for hi in he.items():
                    jj=pau(int(hi[0][-1])-1,masters[ha[0][0]])
                    ss=pau(int(hi[0][-1])-2,masters[ha[0][0]])

                    he[hi[0]]=hi[1]*(jj-ss)
                    ne[hi[0]]=hi[1]*jj
                suma=sum(he[x] for x in he)
                zuma=sum(ne[y] for y in ne)
            
                sumas.append(suma)
                zumas.append(zuma)
            #print("SUMAS PRACTICAS DELTA ",sumas)
            #print("SUMAS PRACTICAS X ",zumas)
            sumas2=[]
            zumas2=[]
            for rie in sumas:
                quie=pau(len(masters[ha[0][0]])-sumas[::-1].index(rie),masters[ha[0][0]])-pau(len(masters[ha[0][0]])-(sumas[::-1].index(rie)+1),masters[ha[0][0]])
                rie=lim(rie,quie)
                sumas2.append(rie)
            for rio in zumas:
                rio=lim(rio,pau(len(masters[ha[0][0]])-zumas[::-1].index(rio),masters[ha[0][0]]))
                zumas2.append(rio)
            feo=sum(sumas2)
            fea=sum(zumas2)
            por_tipos_completo[ha[0]]=feo
            retenciones_gamma[ha[0]]=fea
    por_tipos_completo_ordenado=dict(sorted(por_tipos_completo.items(), key=operator.itemgetter(1)))
    materia_priori=(list(por_tipos_completo_ordenado.keys())[0])
    #print("MATERIA PRIORI", materia_priori)
    print("4444444444444444444",contador_bruto)
    reten=[]
    
    for a in range(1,(dict(fechas_ordenadas)[materia_priori[0]])+1):
        delt=fechas_de_examenes[materia_priori[0]]-timedelta(days=a)
        if materia_priori[1]=="T":
            reten.append({("T2a",delt):T2a(a),("T1b",delt):T1b(a),("T2b",delt):T2b(a),("T1c",delt):T1c(a),("T2c",delt):T2c(a),("T3a",delt):T3a(a),("T3b",delt):T3b(a),("T4b",delt):T4b(a),("T3c",delt):T3c (a),("T4c",delt) :T4c(a),("T3d",delt):T3d (a),("T4d",delt):T4d (a)})
        elif materia_priori[1]=="P":
            reten.append({("P1b",delt):P1b(a),("P2b",delt):P2b(a),("P1c",delt):P1c(a),("P2c",delt):P2c(a),("P3b",delt):P3b(a),("P3c",delt):P3c(a),("P4b",delt):P4b (a),("P4c",delt):P4c(a),("P4d",delt):P4d (a),("P3d",delt): P3d(a)})
    ordenado=(dict(sorted(dict((concatenar(reten))).items(), key=itemgetter(1), reverse=True)))
    tr_disponibles={}
    for ab in ordenado.items():
        if ab[0][1].date() in list(dias_y_espacios_disponibles.keys()):
            tr_disponibles[(ab[0][0],ab[0][1])]=ab[1]

    nros_letras={"a":1,"b":2,"c":3,"d":4}
    tr_disponibles_final={}
    #print(dias_y_espacios_disponibles)
    #dias_y_espacios_disponibles[datetime(2022,11,3).date()]=[0,0,0,0]
    #print(dias_y_espacios_disponibles)
    for ac in tr_disponibles.items():

        if materia_priori[1]=="T":
            
            tiempo_gasto=tiempos_cuartos_teoricos[int(ac[0][0][-2])]
            
            tiempo_disponible=(dias_y_espacios_disponibles[ac[0][1].date()])[nros_letras[ac[0][0][-1]]-1]
            #print("TIEMPO DISPONIBLE", tiempo_disponible)
#            print("TIEMPO GASTO", tiempo_gasto)
            if tiempo_disponible>tiempo_gasto:

                tr_disponibles_final[ac[0]]=ac[1]
        if materia_priori[1]=="P":
            tiempo_gasto=tiempos_cuartos_practicos[int(ac[0][0][-2])]
    #       print(ac)
            tiempo_disponible=(dias_y_espacios_disponibles[ac[0][1].date()])[nros_letras[ac[0][0][-1]]-1]
    #       print(type(tiempo_disponible))
#            print("TIEMPO DISPONIBLE", tiempo_disponible)
#            print("TIEMPO GASTO", tiempo_gasto)
            if tiempo_disponible>tiempo_gasto:
                tr_disponibles_final[ac[0]]=ac[1]
    #print("DISPONIBLES PERO NO CON DIVISION POR TIEMPO NI AUTORES",tr_disponibles_final)
    for poe in tr_disponibles_final.items():
        contador_bruto9=contador_bruto.copy()
        deo={}
        deo[poe[0][1]]=poe[0][0][1:3]
        doe= contador_bruto[materia_priori]
        doi = defaultdict(list)
        for k, v in chain(deo.items(), doe.items()):
            if type(v)==list:
                print("EXISTEEEE")
                v=v[0]
            doi[k].append(v)   
        contador_bruto9[materia_priori]=dict(doi)
        contador9=contador_bruto9.copy()
        for t in contador9.items():
            p={}
            contador9[t[0]]=p
        
            a=sorted(t[1])
            for n in a:
                p[n]=(t[1])[n]
        contador_solo_ordenado9=contador9.copy()

        for y in contador9.items():
            r={}    
            for i in (y[1]).items():
                #print(i)
                r[i[0]]=((sorted(i[1]))[0])
            contador9[y[0]]=r   
    
        contador_fechas9={}
        contador_tipos9={}
        for s in contador9.items():
            if s[0][1]=="T":
                contador_fechas9[s[0]]=list(s[1].keys())
                g=[]   
                for z in (s[1].values()):
                    g.append(int(str(z)[0]))
                contador_tipos9[s[0]]= g
        ranguitos_dic9={}

        for i in contador_tipos9.items():
            indices9=[]

            a=("".join([str(_) for _ in i[1]])).count("1")
            if a>0:
                indice_lugar_de_1=(("".join([str(_) for _ in i[1]])).find("1")) 
                indices9.append(indice_lugar_de_1)
                for l in range(0,a-1):
                    ind_lugar1=(("".join([str(_) for _ in i[1]])).find("1",indices9[-1]+1))
                    indices9.append(ind_lugar1)
        
            b=("".join([str(_) for _ in i[1]])).count("22")
            if b>0:
                indice_lugar_de_22=(("".join([str(_) for _ in i[1]])).find("22"))+1
                indices9.append(indice_lugar_de_22)
                for m in range(0,b-1):
                    ind_lugar22=(("".join([str(_) for _ in i[1]])).find("22",indices9[-1]+1))

                    indices9.append(ind_lugar22+1)

            if -1 in indices9:
                for k in range(0, indices9.count(-1)):        
                    indices9.remove(-1)


            fechecitas9=[]
            for u in indices9:

                fechecitas9.append((contador_fechas9[i[0]][u]))
            (fechecitas9.sort(reverse=True))

            if len(fechecitas9)==0:
                fechecitas9=[fechas_de_examenes[(str(i[0]))[0]]]+fechecitas9+[datetime.now()-timedelta(days=30)]
            else:
                fechecitas9=fechecitas9+[datetime.now()-timedelta(days=30)]
            ranguitos9=[]
            for t in range(0,len(fechecitas9)-1):
                ranguitos9.append([fechecitas9[t],fechecitas9[t+1]+timedelta(days=1)])

            for r in contador9.keys():
                ranguitos_dic9[f"{i[0][0]}{i[0][-1]}"]=ranguitos9

        contador_en_ranguitos9=contador_solo_ordenado9.copy()
        for t in contador_solo_ordenado9.items():

            b=[]
            contador_en_ranguitos9[t[0]]=b

        
            for q in ranguitos_dic9[f"{t[0][0]}{t[0][-1]}"]:
                a={}
          
                for u in (list(t[1].keys())):

                    if  q[0]>=u>=q[-1]:
                        a[u]=t[1][u]
       
                b.append(a)
        for n in contador_en_ranguitos9.items():
            contador_en_ranguitos9[n[0]]=(list(n[1]))[::-1]
        for wa in contador_en_ranguitos9.items():
            esa9=wa[1].copy()
            for we in wa[1]:
                for wi in we.items():
                    esalista9=wi[1].copy()
                    for wo in wi[1]:
                        if len(wo)<4:
                            rui=wa[1].index(we)
                            esalista9[esalista9.index(wo)]=f"{wo}-{len(masters[wa[0][0]])-wa[1][::-1].index(we)}"
                            we[wi[0]]=esalista9
                            wa[1][rui]=we
        por_tipos_completo9={}
        for pa in contador_en_ranguitos9.items():
            hola=[]
            for pe in pa[1]:
                invertido9=defaultdict(list)
                {invertido9[tuple(v)].append(k) for k , v in pe.items()}
                resultado=dict(invertido9)
                eso=[]
            
                for pi in resultado.items():
                    for po in pi[0]:
                        d=(po,pi[1])
                    
                        eso.append(d)
                dict39 = defaultdict(list)
                for k, v in eso:
                    dict39[k].append(v[0])
                kire=dict(dict39)                    
                por_tipos9=kire
                hola.append(por_tipos9)
            por_tipos_completo9[pa[0]]=hola
        copia_tcompleto9=por_tipos_completo9.copy()
        for ga in por_tipos_completo.items():
            for ge in ga[1]:
                geg={}
                for gi in ge.items():
                    if ga[0][1]=="T":
                        if gi[0][0:2]=="1a":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T1a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="2a":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T2a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="1b":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T1b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="2b":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T2b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="1c":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T1c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="2c":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T2c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="3a":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T3a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="3b":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T3b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="4a":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T4a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="4b":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T4b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="3c":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T3c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="4c":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T4c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="3d":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T3d(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="4d":
                            l=[]
                            for go in gi[1]:                   
                                l.append(T4d(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                    if ga[0][1]=="P":
                        if gi[0][0:2]=="1a":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P1a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="2a":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P2a(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="1b":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P1b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="2b":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P2b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="1c":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P1c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="2c":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P2c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="3b":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P3b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="3c":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P3c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="4b":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P4b(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="4c":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P4c(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="4d":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P4d(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
                        if gi[0][0:2]=="3d":
                            l=[]
                            for go in gi[1]:                   
                                l.append(P3d(abs(int((fechas_de_examenes[ga[0][0]]-go).days))))                    
                            ge[gi[0]]=sum(l)
    #print(por_tipos_completo)
        print("33333333333333333333",contador_bruto)
        for nea in por_tipos_completo9.items():
            neo_lista=[]
            for nee in nea[1]:
                print(nee)
                chi={}
                claves=[]
                for nei in nee.items():
                    
                    clave= f"{nei[0][0]}-{nei[0][-1]}"
                    claves.append(clave)
                for neii in set(claves):
                    lista_chi=[]
                    for neo in nee.items():
                        if f"{neo[0][0]}-{neo[0][-1]}"==neii:
                            valor=neo[1]
                            lista_chi.append(valor)
                    #print(neii, sum(lista_chi))
                    #print("limite", limites[nea[0][1]][int(neii[0])-1])
                    #print()
                    
                    chi[neii]=lim(sum(lista_chi),limites[nea[0][1]][int(neii[0])-1])
                neo_lista.append(chi)
            por_tipos_completo9[nea[0]]=neo_lista
        retenciones_gamma9=por_tipos_completo9.copy()  
        for ha in por_tipos_completo9.items():
            if (ha[0][1])=="T":
                sumas=[]
                zumas=[]
                for he in ha[1]:
                    ne=he.copy()
                    for hi in he.items():
                        jj=tau(int(hi[0][-1]),masters[ha[0][0]])
                        ss=tau(int(hi[0][-1])-1,masters[ha[0][0]])
                        he[hi[0]]=hi[1]*(jj-ss)
                        ne[hi[0]]=hi[1]*jj
                    suma=sum(he[x] for x in he)
                    zuma=sum(ne[y] for y in ne)
                    sumas.append(suma)
                    zumas.append(zuma)
                sumas2=[]
                zumas2=[]

                for rie in sumas:
                    ##LE SUME MAS 1
                    quie=tau(len(masters[ha[0][0]])-sumas[::-1].index(rie),masters[ha[0][0]])-tau(len(masters[ha[0][0]])-(sumas[::-1].index(rie)+1),masters[ha[0][0]])
                    rie=lim(rie,quie)
                    sumas2.append(rie)
                for rio in zumas:
                    ##LE SUME MAS 1
                    
                    rio=lim(rio,tau(len(masters[ha[0][0]])-zumas[::-1].index(rio),masters[ha[0][0]]))
                    zumas2.append(rio)
                feo=sum(sumas2)
                fea=sum(zumas2)
                por_tipos_completo9[ha[0]]=feo
                retenciones_gamma9[ha[0]]=fea
            if ha[0][1]=="P":
                sumas=[]
                zumas=[]
                for he in ha[1]:
                    ne=he.copy()
                    for hi in he.items():
                        jj=pau(int(hi[0][-1]),masters[ha[0][0]])
                        ss=pau(int(hi[0][-1])-1,masters[ha[0][0]])
                        he[hi[0]]=hi[1]*(jj-ss)
                        ne[hi[0]]=hi[1]*jj
                    suma=sum(he[x] for x in he)
                    zuma=sum(ne[y] for y in ne)
                    sumas.append(suma)
                    zumas.append(zuma)
                sumas2=[]
                zumas2=[]
                for rie in sumas:
                    ##LE SUME MAS 1
                    
                    quie=pau(len(masters[ha[0][0]])-sumas[::-1].index(rie),masters[ha[0][0]])-pau(len(masters[ha[0][0]])-(sumas[::-1].index(rie)+1),masters[ha[0][0]])
                    rie=lim(rie,quie)
                    sumas2.append(rie)
                for rio in zumas:
                    ##LE SUME MAS 1
                    rio=lim(rio,pau(len(masters[ha[0][0]])-zumas[::-1].index(rio),masters[ha[0][0]]))
                    zumas2.append(rio)
                feo=sum(sumas2)
                fea=sum(zumas2)
            por_tipos_completo9[ha[0]]=feo
            retenciones_gamma9[ha[0]]=fea
        por_tipos_completo_ordenado9=dict(sorted(por_tipos_completo9.items(), key=operator.itemgetter(1)))
        #print("GAMA NUEVO",retenciones_gamma9[materia_priori])
        #print("GAMA, ANTIGUO",retenciones_gamma[materia_priori])
        xdd=retenciones_gamma9[materia_priori]-retenciones_gamma[materia_priori]
        
        if materia_priori[1]=="T":
            xd=xdd/tiempos_cuartos_teoricos[int(poe[0][0][1])]
        elif materia_priori[1]=="P":
            xd=xdd/tiempos_cuartos_practicos[int(poe[0][0][1])]
        tr_disponibles_final[poe[0]]=xd
    disponibles_en_orden = dict(sorted(tr_disponibles_final.items(), key=operator.itemgetter(1), reverse=True))
    #print("DISPONIBLES EN ORDEN",disponibles_en_orden)
    print("55555555555555",contador_bruto)
    #print("TIPOS DE REAPSO DISPONIBLES FINAL EN ORDEN",disponibles_en_orden)
    bro=list(disponibles_en_orden.items())[0]
    #print("SOY BRO", bro)
    z1=contador_bruto[materia_priori]
    ###print("DICCIONARIO ANTIGUO",z1)
    z2={bro[0][1]:[bro[0][0][1:3]]}
    ###print("DICCIONARIO PARA SUMAR ",z2)
    z3 = defaultdict(list)
    for k, v in chain(z1.items(), z2.items()):
 
        z3[k].append(v)
    kira=dict(z3)
    #print("kiralist",kira)
    for killer in kira:
        kira_list=kira[killer]

        kira_list_complete=[]
        for love in kira_list:
            for hate in love:
                kira_list_complete.append(hate)
    #print("LLAVES",z2.keys())
        kira[killer]=kira_list_complete
        contador_bruto[materia_priori]=kira
 

    
    ###print("NUEVO DICCIONARIO",kira)
    ##############print("CONTADOR BRUTO DESPUES DE AGREGAR",contador_bruto)
    contador=contador_bruto.copy()
    for t in contador.items():
        p={}
        contador[t[0]]=p
        a=sorted(t[1])
        for n in a:
            p[n]=(t[1])[n]
    contador_solo_ordenado=contador.copy()
    for y in contador.items():
        r={}    
        for i in (y[1]).items():
            r[i[0]]=((sorted(i[1]))[0])
        contador[y[0]]=r   
    contador_fechas={}
    contador_tipos={}
    for s in contador.items():
        if s[0][1]=="T":
            contador_fechas[s[0]]=list(s[1].keys())
            g=[]   
            for z in (s[1].values()):
                g.append(int(str(z)[0]))
            contador_tipos[s[0]]= g 
    ranguitos_dic={}
    for i in contador_tipos.items():
        indices=[]

        a=("".join([str(_) for _ in i[1]])).count("1")
        if a>0:
            indice_lugar_de_1=(("".join([str(_) for _ in i[1]])).find("1")) 
            indices.append(indice_lugar_de_1)
            for l in range(0,a-1):
                ind_lugar1=(("".join([str(_) for _ in i[1]])).find("1",indices[-1]+1))
                indices.append(ind_lugar1)
        
        b=("".join([str(_) for _ in i[1]])).count("22")
        if b>0:
            indice_lugar_de_22=(("".join([str(_) for _ in i[1]])).find("22"))+1
            indices.append(indice_lugar_de_22)
            for m in range(0,b-1):
                ind_lugar22=(("".join([str(_) for _ in i[1]])).find("22",indices[-1]+1))

                indices.append(ind_lugar22+1)

        if -1 in indices:
            for k in range(0, indices.count(-1)):        
                indices.remove(-1)


        fechecitas=[]
        for u in indices:
            fechecitas.append((contador_fechas[i[0]][u]))
        (fechecitas.sort(reverse=True))

        if len(fechecitas)==0:
            fechecitas=[fechas_de_examenes[(str(i[0]))[0]]]+fechecitas+[datetime.now()-timedelta(days=30)]
        else:
            fechecitas=fechecitas+[datetime.now()-timedelta(days=30)]

        ranguitos=[]
        for t in range(0,len(fechecitas)-1):
            ranguitos.append([fechecitas[t],fechecitas[t+1]+timedelta(days=1)])

        for r in contador.keys():
            ranguitos_dic[f"{i[0][0]}{i[0][-1]}"]=ranguitos

    contador_en_ranguitos=contador_solo_ordenado.copy()
    for t in contador_solo_ordenado.items():
        b=[]
        contador_en_ranguitos[t[0]]=b
        for q in ranguitos_dic[f"{t[0][0]}{t[0][-1]}"]:
            a={}
            for u in (list(t[1].keys())):
                if  q[0]>=u>=q[-1]:
                    a[u]=t[1][u]
            b.append(a)
    for n in contador_en_ranguitos.items():
        contador_en_ranguitos[n[0]]=(list(n[1]))[::-1]


    for wa in contador_en_ranguitos.items():
        esa=wa[1].copy()
        for we in wa[1]:
            for wi in we.items():
                esalista=wi[1].copy()
                for wo in wi[1]:
                    if len(wo)<4:
                        rui=wa[1].index(we)
                        xa=len(masters[wa[0][0]])-wa[1][::-1].index(we)
                        xe=f"{wo}-{xa}"
                        esalista[esalista.index(wo)]=xe
                        we[wi[0]]=esalista
                        wa[1][rui]=we
                        #print("HOLA SOY XE, EL ULTIMO AUTOR",xa)
    #print("DIAS Y ESPACIOS DISPONIBLES 2", dias_y_espacios_disponibles)
    rock=f"{materia_priori}-{xe}"
    #print(rock)
    lesta=agenda[bro[0][1].date()]
    #print(lesta)
    lesta.append(rock)
    agenda[bro[0][1].date()]=lesta
    lista24=dias_y_espacios_disponibles[bro[0][1].date()]
    #print("CONTADOR BRUTO FINAL",contador_bruto)
    valor25=dias_y_espacios_disponibles[bro[0][1].date()][nros_letras[bro[0][0][2]]-1]
    if materia_priori[1]=="T":
        valor26=tiempos_cuartos_teoricos[int(bro[0][0][1])]
    if materia_priori[1]=="P":
        valor26=tiempos_cuartos_practicos[int(bro[0][0][1])]
    valor27=valor25-valor26
    lista24[lista24.index(valor25)]=valor27
    dias_y_espacios_disponibles[bro[0][1].date()]=lista24
    #print("DIAS Y ESPACIOS DISPONIBLES 3",dias_y_espacios_disponibles)
    #print(por_tipos_completo)
    if xe[-1]=="1":
        cl_de_materias[materia_priori]=1
    #print(cl_de_materias)
    if (list(set(cl_de_materias.values())))==[1]:
        break
    if sum(dias_y_espacios_disponibles[(datetime.now()+timedelta(days=1)).date()])<40:
        break
print("MI AGENDA",agenda)    
print("VE POR ELLOS TIGRE")
print(por_tipos_completo)

