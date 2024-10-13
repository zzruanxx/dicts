
# Exemplo de dicionário
pessoa = {
    "nome": "Rudolph",
    "idade": 84,
    "cidade": "Lisboa",
    "hobbies": ["trilhas", "música", "dança"],
    "empregado": True
}

# Acessando valores do dicionário
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
print("Hobbies:", ", ".join(pessoa["hobbies"]))
print("Empregado:", pessoa["empregado"])
