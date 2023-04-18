idade : int
salario : float
nome : str
sexo : str


nome = input("Informe o nome do funcionario: ")
salario = float(input("Informe o valor recebido pelo funcionario: "))
idade = int(input("Informe a idade do funcionario: "))
sexo = input("Informe o sexo do funcionario: (Masculino/Feminino) ")

print(f"O funcionario {nome}, recebe R$ {salario:.2f}, do sexo {sexo} e tem {idade} anos. ")


