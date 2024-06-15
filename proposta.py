from moda import modaSalario
# from mediana import medianaSalario
# from desvio import desvioSalario
# from media import mediaSalario


empresaItau = [1000,6000,1200,8000,1400]
empresaBradesco = [5000,4000,3000,2000,7000]
empresaC6 = [1200,1300,8000,3000,15000]
empresaGoogle = [1400,1750,2000,4500,5900,7000]

# def propostaSalario(lista, salario):
#     print("o nome da empresa :" , salario)


def hadle(lista, salarios):

    print('EMPRESA', salarios)
    print('----------------------------')
    mediaSalario(lista)
    medianaSalario(lista)
    modaSalario(lista)