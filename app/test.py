from db import historico_compras

resultados = list(historico_compras.find({}, {'_id': 0}))
total = 0.0
for item in resultados:
    valor_item = item["valor_total"]
    print(valor_item)
    total += float(valor_item.replace(",", "."))
print(total)