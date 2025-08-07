import requests
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