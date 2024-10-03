nombre = input(" Ingrese su nombre: ")
diasTrabajo = int(input(" Ingrese sus dias de trabajo "))
salario = int(input( "Ingrese su salario "))

#Calcular Prima

result= salario*diasTrabajo/360

#calcularCesantías

result2 = salario * diasTrabajo/360

#calcularIntereses

result3 = result2 * 0.12/diasTrabajo

#calcularVacaiones

result4 = salario *diasTrabajo/720

print( f" Señor {nombre} para los {diasTrabajo} días laborados "
       
       f" y salario $ {salario} su loquidacion se compone asi:"
       
       f"Prima: ${result}"
       
       f" Cesantía: ${result2:2f}"
       
       f"Intereses cesantías: ${result3}"
       
       f"Vacaciones: ${result4:2f}"
       
       f"Liquidación:")
