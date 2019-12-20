# FUNCIONES01
def distancia(velocidad,tiempo):
    respuesta=velocidad*tiempo
    return respuesta
# fin_def


# FUNCIONES02

def pedir_velocidad_final(velocidad_inicial,aceleracion,tiempo):
    velocidad_final=velocidad_inicial+(aceleracion*tiempo)
    return velocidad_final
# fin_def


# FUNCIONES03
def promedio(nota01,nota02,nota03,nota04):
    promedio_final=(nota01+nota02+nota03+nota04)/4
    return promedio_final
# fin_def


# FUNCIONES04
def volumen_esfera(pi,radio):
    volumen=(pi*radio*radio*radio*4)/3
    return volumen
# fin_def


# FUNCIONES05
def dividendo(divisor,cociente,residuo):
    dividendo=(divisor*cociente)+residuo
    return dividendo
# fin_def


# FUNCIONES06
def area_trapecio(base_mayor,base_menor,altura):
    area=(base_mayor+base_menor)*altura/2
    return area
# fin_def


# FUNCIONES07
def fuerza(masa,longitud,tiempo):
    fuerza=(masa*longitud)/(tiempo**2)
    return fuerza
# fin_def


# FUNCIONES08
def  fuerza_centripeta(masa,velocidad,radio):
    resultado=masa*(velocidad**2)/radio
    return resultado
# fin_def


# FUNCIONES09
def altura(velocidad_inicial,tiempo,gravedad):
    altura=velocidad_inicial*tiempo +(gravedad*(tiempo**2))/2
    return altura
# fin_def


# FUNCIONES10
def presion(densidad_liquido,gravedad,altura):
    presion=densidad_liquido*gravedad*altura
    return presion
# fin_def


# FUNCIONES11
def nombre_completo(nombre1,nombre2,apellido1,apellido2):
    resultado1=nombre1
    resultado2=nombre2
    resultado3=apellido1
    resultado4=apellido2
    return (resultado1+" "+" "+resultado2+" "+" "+resultado3+" "+" "+resultado4)
# fin_def


# FUNCIONES12
def total_precio(precio_final):
    precio_final=0
    return precio_final
# fin_def


# FUNCIONES13
def boleta(cantidad_arroz,cantidad_azucar,cantidad_fideo,precio_arroz,precio_azucar,precio_fideo):
    total_pagar=(cantidad_arroz*precio_arroz)+(cantidad_azucar*precio_azucar)+(cantidad_fideo*precio_fideo)
    return float(total_pagar)
# fin_def


# FUNCIONES14
def temperatura(presion,volumen,mol,constante):
    return (presion*volumen)/(mol*constante)
# fin_def


# FUNCIONES15
def variacion_longitud(x,y,z):
    return x*y*z
# fin_def


# FUNCIONES16
def calor_especifico(x,y,z):
    return (x*y)/z
# fin def


# FUNCIONES17
def suma_par(x,y,z,w):
    if (x,y,z,w %2 ==0):
        return (x+y+z+w)
# fin_def


# FUNCIONES18
def suma_impar(a,b,c,d):
    if (a,b,c,d %2 != 0):
        return (a+b+c+d)
# fin_def


# FUNCIONES19
def eficiencia(n,r):
    return (n-r)/n
# fin_def


# FUNCIONES20
def campo_electrico(a,b,s):
    return (a*b)/(s**2)
# fin_def


# FUNCIONES21
def fuerza_electrica(a,b,c,d):
    return (a*b*c)/(d**2)
# fin_def


# FUNCIONES22
def ley_poulet(m,n,p):
    return (m*n)/p
# fin_def


# FUNCIONES23
def dividir(x,y,z,f,g):
    return (x+y+z+f+g)/(x*g)
# fin_def


# FUNCIONES24
def operacion(m,n,o,p,q,r):
    return (m+m+n+r+r+q)*(m*o*r)/(p*o)
# fin_def


# FUNCIONES25
def funcion(x,y,z,w,m):
    respuesta=(x,y,z,w,m)
    if(respuesta == "888"):
        return "ES VERDADERA"
    else:
        return "ES FALSA"

# fin_def
