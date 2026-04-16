# ex7 (✿◠ᴗ◠)
 
nota1=int(input("diga a nota do prova 1: "))
nota2=int(input("diga a nota do prova 2: "))
nota3=int(input("diga a nota do prova 3: "))
 
prova1=2
prova2=3
prova3=5
 
soma=prova1+prova2+prova3
med=((nota1*prova1 + nota2*prova2+nota3*prova3)/soma)
 
if med >= 6:
    print("média : ",med, "\naprovado")
elif med <6:
    print("média : ",med, "\nreprovado")