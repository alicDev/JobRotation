valores = [221741664, 245376698, 261396134, 0.0, 0.0, 267426612, 0.0, 42889.2258, 46251.174, 111914722
, 0.0, 0.0, 38474823, 3737838, 2659.7563, 489242448, 184192614, 0.0, 0.0, 352401826, 438291667, 182356852
, 43550662, 133271025, 0.0, 0.0, 256818318, 17181221, 13220495, 841461 ]

print('O menor valor de faturamento ocorrido em um dia do mês: ', min(valores))
print('O maior valor de faturamento ocorrido em um dia do mês: ', max(valores))
media = (sum(valores)) / 30
count = 0
for i in valores:
    if i > media:
        count += 1
print(f'Dias no mês em que o valor de faturamento diário foi superior à média mensal: {count}')