import requests
from bs4 import BeautifulSoup

url = "https://www.nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?p=35250547508411268639650040002292871688392510|2|1|1|7182E60B22C4A73C4D115D98F4207390EFF8FC78"
url3 = "https://www.nfce.fazenda.sp.gov.br/qrcode?p=35250547508411268639650040002292871688392510|2|1|1|7182E60B22C4A73C4D115D98F4207390EFF8FC78"
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
