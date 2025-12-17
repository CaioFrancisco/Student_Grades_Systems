# --- Entrada ---
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
nota3 = float(input("Digite a terceira nota ( 0 a 10): "))
nota4 = float(input("Digite a quarta nota ( 0 a 10): "))
prova_extra = float(input("Digite a nota da prova extra (peso 2) (0 a 10): "))
presenca = int(input("Digite a presenca em % (0 a 100): "))
# --- Processamento ---
media = (nota1 + nota2 + nota3 + nota4 + prova_extra * 2) / 6
media = media + 0.5
# --- Operação relacionada e lógica ---
aprovado_media = media >= 7
tem_presenca = presenca >= 75
em_recuperacao = (media >= 5) and (media < 7) and tem_presenca
# --- Decisao Final ---
if aprovado_media and tem_presenca:
    situacao = "APROVADO"
elif em_recuperacao:
    situacao = "RECUPERACAO"
else:
    situacao = "REPROVADO"
# --- Saída ---
print("\n--- RESULTADO FINAL ---")
print("Notas: ", nota1, nota2, nota3, nota4)
print("Prova extra (peso 2): ", prova_extra)
print("Presenca: ", presenca, "%")
print("Media final (com bonus): ", media)
print("Aprovado em media?", aprovado_media)
print("Tem presenca minima (>= 75%)?", tem_presenca)
print("Situacao final do aluno: ", situacao)
