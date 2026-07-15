aluno = {
    "nome": "Lucas Silva",
    "idade": 16,
    "notas": [8.5, 7.0, 9.2]
}

print("--- Dados do Aluno ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {aluno['notas']}")

media = sum(aluno['notas']) / len(aluno['notas'])
print(f"Média do Aluno: {media:.2f}")