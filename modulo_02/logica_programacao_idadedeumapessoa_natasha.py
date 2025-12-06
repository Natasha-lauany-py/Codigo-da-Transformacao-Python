# Solicita a idade ao usuário
idade = int(input("Digite sua idade: "))

# Classifica a idade em categorias
if idade < 12:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Idoso"

# Exibe a categoria
print(f"Você é classificado(a) como: {categoria}")

