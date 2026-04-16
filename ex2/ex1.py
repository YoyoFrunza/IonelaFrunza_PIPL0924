# ex1 (✿◠ᴗ◠)

segundos = int(input("segundos: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_finais = resto % 60

print(horas, "hora(s),", minutos, "minuto(s) e", segundos_finais, "segundo(s)")