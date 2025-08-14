import requests
import re
import cv2
from bs4 import BeautifulSoup
from pyzbar.pyzbar import decode

# Leitura do QR Code
img = cv2.imread("../files/qr_code_2.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
results = decode(img)

for obj in results:
    print(obj.data.decode("utf-8"))

# Acessando internet
url = results[0].data.decode("utf-8")
headers = {
    "User-Agent": "Mozilla/5.0",  # Para parecer um navegador real
}

response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
registros = soup.find_all('tr')

for registro in registros:
    print(f"Produto: {registro.find(class_= 'txtTit').text}")
    print(f"Quantidade: {registro.find(class_= 'Rqtd').text}")
    print(f"Valor: {registro.find(class_= 'valor').text}")

texto_cnpj = soup.find(id="conteudo").find_all("div")[1].find_all("div")[1].text
cnpj_formatado = re.sub(r'\D', '', texto_cnpj)

texto_endereco = soup.find(id="conteudo").find_all("div")[1].find_all("div")[2].get_text(strip=True)
endereco_formatado = re.sub(r'[\t\n\r]', '', texto_endereco)

print(f"Estabelecimento: {soup.find(id="u20").text}")
print(f"CNPJ: {cnpj_formatado}")
print(f"Endereço: {endereco_formatado}")

totais_numeros = soup.find(id="totalNota").find_all(class_="totalNumb")
totais_textos = soup.find(id="totalNota").find_all(class_="tx")
qtd_total_itens = totais_numeros[0].text
valor_total = totais_numeros[1].text
descontos = totais_numeros[2].text
valor_a_pagar = totais_numeros[3].text
valor_pago = totais_numeros[5].text
troco = totais_numeros[6].text
forma_pagamento = totais_textos[0].text
forma_pagamento = re.sub(r'[\t\n\r]', '', forma_pagamento)


print(f"qtd_total_itens: {qtd_total_itens}")
print(f"valor_total: {valor_total}")
print(f"descontos: {descontos}")
print(f"valor_a_pagar: {valor_a_pagar}")
print(f"valor_pago: {valor_pago}")
print(f"troco: {troco}")
print(f"forma_pagamento: {forma_pagamento}")
# Quantidade total de itens
# Valor total
# Descontos
# Valor a pagar
# Forma de pagamento
# Valor pago
# Troco
# Horário emissão
# Data emissão
# Nome estabelecimento
# CNPJ
# Endereço
# Consumidor (não identificado)