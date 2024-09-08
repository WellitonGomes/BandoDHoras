def obterInformacoes():
    HorasTR = int(input("Por favor, informe a quantidade de horas trabalhadas por dia: "))
    MinutosTR = int(input("Por favor, informe a quantidade de minutos trabalhados: "))
    DiasTR = int(input("Por favor, informe a quantidade de dias trabalhados: "))
    Salario = int(input("Por favor, informe seu salário: "))
    return HorasTR, MinutosTR, DiasTR, Salario

def calcularDados(HorasTR, MinutosTR, DiasTR, Salario):
    HorasM = MinutosTR / 60
    HorasF = HorasTR + HorasM
    HorasMes = HorasF * DiasTR
    Ganho = Salario / HorasMes  

    print("Você ganhará:", Ganho, "reais por hora")


HorasTR, MinutosTR, DiasTR, Salario = obterInformacoes()


calcularDados(HorasTR, MinutosTR, DiasTR, Salario)
