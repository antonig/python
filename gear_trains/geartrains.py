# arreglado
#  porque salen muchas soluciones pero todas son la misma?
#  eliminados engranajes redundantes
#  error pasado a relativo, con signo
#  131/79 da division por cero
#  formatear salida
#  visualizada aprox por funciones continuas con factorizacion
#  factorizacion directa sin tabla de primos
#  cargar ruedas de archivo
#  probar para 1,2,3,4 pares
#  compilar
#  formatear salida (eliminar L)
#  entrada de ordenes usuario
#  bucle principal
#  imprimir tablas de pares

# arreglar
#  invertir fraccion si nume > denom
#  si fraccion tiene demasiadas cifras para tabla, usar continua y sumar errores
#  resumen o todo
#  nueva busqueda
#  
#---------------------------------------------
# pendiente:

#  anadir /quitar ruedas
#  a fichero 

#  visualizar aparte salidas con mismo resultado

#--------------------------------------------
#  futuro
#   gui
#   considerar distancias, sugerir montaje
#   anadir dentados incompatibles (cadenas)
#   anadir diferenciales
#   anadir epicicloidal
#   


from fractions import *
import itertools
import math
import sys
import copy
import bisect
import operator

from functools import reduce

nums=set('0123456789')


'''
ratios= [7,10,11,12,13,15,16,17,19,20,22,24,25,26,27,28,30,38,45,55,56,57,60,
         65,66,70,76,95,133,152,171]
'''


def isnumber(s):
   try:
     float(s)
     return True
   except ValueError:
     try: 
       Fraction(s)
       return True
     except ValueError: 
       return False

def makelist1(r,n=1):
 b=[(reduce(lambda a, b: a*b,x),list(x)) for x in itertools.combinations_with_replacement(r,n)]
 return sorted(b)



def herror(exact,aprox): return float(aprox-exact)/exact

def contfracra(x,y):
  c2,d2,c1,d1,b2,b1,b=0,1,1,0,x,y,1
  l=[]
  while b1:
    b=b2 % b1
    a= b2 // b1
    c=a*c1+c2
    d=a*d1+d2
    e=((c*y)-(d*x))/float(d*x)
    l.append([a,c,d,e])
    b2,b1,c2,c1,d2,d1=b1,b,c1,c,d1,d
  return l

def factorize(n1):
    if n1==0: return []
    if n1==1: return [1]
    n=n1
    b=[]
    while n % 2 ==0 : b.append(2);n//=2
    while n % 3 ==0 : b.append(3);n//=3
    i=5
    inc=2
    lim=int(n**0.5)
    while i<lim:
     while n % i ==0 : b.append(i); n//=i
     i+=inc
     inc=6-inc
    if n!=1:b.append(n) 
    return b 

def removedup(a,b):
            for j in a[:]:
               if j in b:
                  a.remove(j)
                  b.remove(j)
            return a,b

def printproducts():
     prnt=sys.stdout          
     global d
     f1=open('./products.txt', 'w+')
     for i in d:
       f1.write('{:13d}'.format(i[0])+'\t'+' '.join('{:3d}'.format(a) for a in i[1])+'\n')  


def searchratio(t,n,d,e):
   #n debe ser menor o igual que d
   b=[]
   a=float(n)/d
   t0=t[0]
   x1=bisect.bisect(t,t0/a)
   print (a,x1,t0)
   lm=len(t)-2
   #comenzamos por primer d para el que n esta en lista,
   #para todos los n hasta el final
   for ti in t[x1:lm]:
          x1=bisect.bisect_left(t,ti*a)
          b.append([t[x1],ti])
          b.append([t[x1+1],ti])
   b.sort(key = lambda x:abs(x[0]/float(x[1])/a)-a)
   return b   

def calculate1(rat,l,a):
   #d es lista ratios,l es lista aproxIMACIONES,a es ratio buscado
   n=a.numerator
   d=a.denominator
   t=[k[0] for k in rat]
    #si n<d invertir
   swap=0
   if n>d: swap=1
  
   #if d>t[len(t)/3] then
    
  
   #si d> 1/3 tabla, buscar desarrollo anterior,
   #llamar searchratio añadir error
   #si habiamos invertido, invertir resultados
   
   #si mas de 100 resultados, limitar a 1e-3
   #buscar combinaciones correspondientes a productos?
   #removedup
   pass



def searcharatio1(l,a,n,d):
   
   b=[]
   #productos
   t=[k[0] for k in l]
  
   ma,mi =a.numerator, a.denominator
   if mi>ma :
        ma,mi=mi,ma
   maxt=t[len(t)-1]
   x1,x2=0,0
   lastx1=0
   lastx2=0 
   for ti in t:
          i=int(math.ceil(float(ti)/mi))
          if ma*i> maxt:
            break
          x1=bisect.bisect(t,n*i)
          x2=bisect.bisect(t,d*i)
          n1, n2, d1, d2= x1-1,min(x1,len(t)-1), x2-1,min(x2,len(t)-1)
          r=min([(n1,d1),(n2,d1),(n1,d2),(n2,d2)],key= lambda x:abs(float(t[x[0]])/t[x[1]]-a))
          b1=r[0] ; b2=r[1] 
          if b1!=lastx1 or b1!= lastx2:
            lastx1, lastx2=b1,b2
            a1,a2=l[b1][1],l[b2][1] 
            a3,a4= removedup(copy.copy(a1),copy.copy(a2))
            herr=herror(float(t[b1])/t[b2],a)
            line=[herr,tuple(a3),tuple(a4)]
            #if line not in b:
            b.append(line)
           
   b_set = set(tuple(x) for x in b)
   b= [ list(x) for x in b_set ]
   b.sort(key = lambda s:(abs(s[0]),s[0], len(s[1])))
   return b

def calculate(d,l,a):
    inv=0
    minr=d[0][0]
    maxr=d[-1][0]
    return searcharatio1(d,a,a.numerator,a.denominator)
   
def printratios (e1,n,mx):
    prnt=sys.stdout           
    e= list(filter(lambda x: len(x[1])==n,e1))
    cnt,a1 =0,99999
    prnt.write( '\n------------------------------------------------------------\n')
    prnt.write( '{:d} Results with {:d} pairs \n'.format(len(e),n))
    for i in e:
      a= i[0]
      if cnt>=mx: break
      if a1!=a:
         prnt.write( '\n')
         x=Fraction(reduce(lambda x,y:x*y,i[1]),reduce(lambda x,y:x*y, i[2]))
         prnt.write( 'error : {:+9.2e} ratio: {:9d}/{:<9d} \n'.format (i[0],x.numerator,x.denominator))
         a1=a
      cnt+=1   
      prnt.write( 'In: {:>20s}'.format(''.join('{:4d}'.format(k) for k in i[1]))+
                  '   Out: {:>20s}\n'.format(''.join('{:4d}'.format(k) for k in i[2])) )
    
    
def printratios2(e,nr):
   global nprod
   prnt=sys.stdout
   if len(e):
     prnt.write( '\n\n')
     prnt.write( '{:d} results\n'.format(len(e)))
     if e[0][0]==0.0:
        prnt.write( 'found exact results\n')
         
     else:
        prnt.write( 'no exact results. Best match {:+9.2e}\n'.format (e[0][0]))   
         
     for i in range(1,nprod+1):   
         printratios(e,i,nr)
   
   else:
     prnt.write( " numerator and/or denominator too big for the present table\n")

def vervalores(a,l):
   prnt=sys.stdout
   prnt.write('\n')

   prnt.write( 'Continuous fraction series:\n')
   prnt.write('\n')            
   prnt.write( 'coef        num/denom         error         num_factors denom_factors\n')
   prnt.write( '----        ---------         -----         ----------- --------------\n')    
   prnt.write('\n')
                              
   for x in l:
     i,n1,d1,e =x[0],x[1],x[2],x[3]
     nn=factorize(n1)
     nd=factorize(d1)
     prnt.write( '{:<6d}{:9d}/{:<9d} {:9.2e}'.format(i,n1 ,d1,e)+
                 '{:>20s}'.format(' '.join('{:d}'.format (i) for i in nn))+'/'+
                 ' '.join('{:d}'.format (i) for i in nd)+'\n' )

def helpme():
   prnt=sys.stdout              
   
   prnt.write( """
Gear Rate Calculator 1.0 by Antoni Gual Club Meccano de Catalunya
http://clubmeccanocatalunya.net
Gears considered are those in file gears.txt. 
Converts user input in a fraction and searches numerator and denominator
in a table of products of teethnumbers.
Returns continuous fraction developement and prime factorizations
Use:
   Enter gear rate as a number 2.1212 or as a fraction   123/4354
   =Python_expression to use as a gear rate  (for example =math.sqrt(2))
   p prnt.write(s all results
   h displays this help
   r outputs all products to products.txt\n""")

    
def doratios(a):
    global d
    prnt=sys.stdout           
    l= contfracra(a.numerator,a.denominator)
    vervalores(a,l)
    e =calculate (d,l,a)
    prnt.write( "calculating please wait\n")
    printratios2(e,1)
    prnt.write( "Enter p for complete list\n\n")
    return e

def inputloop():
  global d
  prnt=sys.stdout
  a=0
  e=[]
  prnt.write( '{:d}\n'.format(len(d)))
  while 1:
   prnt.write('') 
   i=input("Enter gear rate: ")
   if len(i)==0:
         sys.exit(0)
   elif i[0]=='h':
      helpme()
   elif i[0]=='p':
         if a!=0:
           printratios2(e,100)
         else:
           prnt.write( 'Can''t print results before doing the first calculation!\n')
   elif i[0]=='r':   
          prnt.write(products())
   elif i[0]=='=':
       try:
          a= Fraction((eval(i[1:]))).limit_denominator(1000000000)
       except:
          prnt.write( "Sorry, I don't understand\n")
       e=doratios(a)      
   elif isnumber(i):
       try:
         a= Fraction(i).limit_denominator(1000000000)
       except:
         prnt.write( "Sorry, I don't understand\n")
       e=doratios(a)  
   else:
       prnt.write( "Sorry, I don't understand\n")
         
def main():
   global d
   global nprod
   prnt=sys.stdout
   nprod=4
   crs = open("gears.txt", "r")
   ratios= [int(line) for line in crs  if line[0] in nums]
   d= makelist1(ratios,nprod)
   helpme()
   inputloop()

if __name__ == "__main__":
    main()


  
  

