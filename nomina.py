#Autor: Cinthia A.
num = int(input("Ingresa el número total de empleados: ")) 
while num == 0:
    int(input("Ingresa el número total de empleados: "))
nominas = []
nomt = 0
for i in range(1,num+1):
    print("Ingresa el sueldo",i,":")
    x = input()
    x = int(x)
    nominas.append(x)
    nomt += x
print("Fin de capturas de nóminas")

print("***NÓMINA***")
n = 1
for elemento in nominas:
    print("Empleado",n,":","$",(elemento))
    n+= 1

m = 1000
q = 500
d = 200
ci = 100
c = 50
v = 20
suma_mt = 0
#mtot = 0
suma_qt = 0
suma_dt = 0
suma_cit = 0
suma_ct = 0
suma_vt = 0
print("Total de nómina: $",nomt)
for elemento in nominas:
    b = (elemento)
    mt = (b // m) 
    b = (b - (mt*m))
    qt = (b // q)
    b = (b - (qt*q))
    dt = (b // d)
    b = (b - (dt*d))
    cit = (b // ci)
    b = (b - (cit*ci))
    ct = (b // c)
    b = (b - (ct*c))
    vt = (b // v)
    b = (b -(vt*v)) 
    if num == 1:
        mt = mt
        qt = qt
        dt = dt
        cit = cit
        ct = ct
        vt = vt
    else:
        suma_mt = suma_mt + mt 
        suma_qt = suma_qt + qt
        suma_dt = suma_dt + dt
        suma_cit = suma_cit + cit
        suma_ct = suma_ct + ct 
        suma_vt = suma_vt + vt
    
print("Desglose de efectivo")
print("$1000 --->",suma_mt,"billetes")
print("$500 --->",suma_qt,"billetes")
print("$200 --->",suma_dt,"billetes")
print("$100 --->",suma_cit,"billetes")
print("$50 --->",suma_ct,"billetes")
print("$20 --->",suma_vt,"billetes")

