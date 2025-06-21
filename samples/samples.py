from datetime import datetime
from zoneinfo import ZoneInfo

produtos = [
  {
    "id_compra": "1747510520102862",
    "nome_produto": "PRODUTO ALIMENTÍCIO",
    "marca": "Desconhecida",
    "categoria": "ALIMENTOS",
    "quantidade_produto": 300,
    "unidade_medida_produto": "g",
    "quantidade": 2,
    "unidade_medida": "UN",
    "valor_unitario": 11.90,
    "valor_total": 23.80,
    "desconto": None,
    "estabelecimento": {
      "nome": "CIA BRASILEIRA DE DISTRIBUICAO",
      "cnpj": "47.508.411/0926-89",
      "cidade": "SÃO CARLOS",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 17, 13, 37, 34, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": None,
      "codigo_nota": "000230954"
    },
    "totais": {
      "valor_total": 45.69,
      "valor_pago": 42.78,
      "forma_pagamento": "CARTAOON"
    }
  },
  {
    "id_compra": "1747510520102862",
    "nome_produto": "UVA",
    "marca": "QA",
    "categoria": "FRUTAS",
    "quantidade_produto": 500,
    "unidade_medida_produto": "g",
    "quantidade": 1,
    "unidade_medida": "UN",
    "valor_unitario": 12.90,
    "valor_total": 12.90,
    "desconto": -2.91,
    "estabelecimento": {
      "nome": "CIA BRASILEIRA DE DISTRIBUICAO",
      "cnpj": "47.508.411/0926-89",
      "cidade": "SÃO CARLOS",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 17, 13, 37, 34, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": None,
      "codigo_nota": "000230954"
    },
    "totais": {
      "valor_total": 45.69,
      "valor_pago": 42.78,
      "forma_pagamento": "CARTAOON"
    }
  },
  {
    "id_compra": "1747510520102862",
    "nome_produto": "REFRIGERANTE",
    "marca": "PEPSI",
    "categoria": "REFRIGERANTES",
    "quantidade_produto": 2,
    "unidade_medida_produto": "L",
    "quantidade": 1,
    "unidade_medida": "UN",
    "valor_unitario": 8.99,
    "valor_total": 8.99,
    "desconto": None,
    "estabelecimento": {
      "nome": "CIA BRASILEIRA DE DISTRIBUICAO",
      "cnpj": "47.508.411/0926-89",
      "cidade": "SÃO CARLOS",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 17, 13, 37, 34, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": None,
      "codigo_nota": "000230954"
    },
    "totais": {
      "valor_total": 45.69,
      "valor_pago": 42.78,
      "forma_pagamento": "CARTAOON"
    }
  },
  {
    "id_compra": "1747510520102862",
    "nome_produto": "ARROZ",
    "marca": "TIO JOAO",
    "categoria": "ALIMENTOS",
    "quantidade_produto": 1,
    "unidade_medida_produto": "kg",
    "quantidade": 1,
    "unidade_medida": "UN",
    "valor_unitario": 15.50,
    "valor_total": 15.50,
    "desconto": None,
    "estabelecimento": {
      "nome": "CIA BRASILEIRA DE DISTRIBUICAO",
      "cnpj": "47.508.411/0926-89",
      "cidade": "SÃO CARLOS",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 17, 13, 37, 34, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": None,
      "codigo_nota": "000230954"
    },
    "totais": {
      "valor_total": 45.69,
      "valor_pago": 42.78,
      "forma_pagamento": "CARTAOON"
    }
  },
  {
    "id_compra": "1747510520102862",
    "nome_produto": "FEIJAO",
    "marca": "CARIOCA",
    "categoria": "ALIMENTOS",
    "quantidade_produto": 500,
    "unidade_medida_produto": "g",
    "quantidade": 1,
    "unidade_medida": "UN",
    "valor_unitario": 7.80,
    "valor_total": 7.80,
    "desconto": None,
    "estabelecimento": {
      "nome": "CIA BRASILEIRA DE DISTRIBUICAO",
      "cnpj": "47.508.411/0926-89",
      "cidade": "SÃO CARLOS",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 17, 13, 37, 34, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": None,
      "codigo_nota": "000230954"
    },
    "totais": {
      "valor_total": 45.69,
      "valor_pago": 42.78,
      "forma_pagamento": "CARTAOON"
    }
  },
  {
    "id_compra": "1747510520102862",
    "nome_produto": "LEITE",
    "marca": "ITAU",
    "categoria": "LATICINIOS",
    "quantidade_produto": 1,
    "unidade_medida_produto": "L",
    "quantidade": 2,
    "unidade_medida": "UN",
    "valor_unitario": 4.50,
    "valor_total": 9.00,
    "desconto": None,
    "estabelecimento": {
      "nome": "CIA BRASILEIRA DE DISTRIBUICAO",
      "cnpj": "47.508.411/0926-89",
      "cidade": "SÃO CARLOS",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 17, 13, 37, 34, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": None,
      "codigo_nota": "000230954"
    },
    "totais": {
      "valor_total": 45.69,
      "valor_pago": 42.78,
      "forma_pagamento": "CARTAOON"
    }
  },
  {
    "id_compra": "1747510520102862",
    "nome_produto": "PÃO FRANCÊS",
    "marca": "PADARIA DO ZÉ",
    "categoria": "PADARIA",
    "quantidade_produto": 6,
    "unidade_medida_produto": "UN",
    "quantidade": 1,
    "unidade_medida": "PACOTE",
    "valor_unitario": 7.00,
    "valor_total": 7.00,
    "desconto": -1.00,
    "estabelecimento": {
      "nome": "CIA BRASILEIRA DE DISTRIBUICAO",
      "cnpj": "47.508.411/0926-89",
      "cidade": "SÃO CARLOS",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 17, 13, 37, 34, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": None,
      "codigo_nota": "000230954"
    },
    "totais": {
      "valor_total": 45.69,
      "valor_pago": 42.78,
      "forma_pagamento": "CARTAOON"
    }
  },
  {
    "id_compra": "202505170001",
    "nome_produto": "Arroz Branco Tipo 1",
    "marca": "Tio João",
    "categoria": "ALIMENTOS",
    "quantidade_produto": 5,
    "unidade_medida_produto": "kg",
    "quantidade": 1,
    "unidade_medida": "UN",
    "valor_unitario": 24.90,
    "valor_total": 24.90,
    "desconto": None,
    "estabelecimento": {
      "nome": "Supermercado Bom Preço",
      "cnpj": "12.345.678/0001-90",
      "cidade": "São Paulo",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 17, 13, 37, 34, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": "12345",
      "codigo_nota": "0010001"
    },
    "totais": {
      "valor_total": 87.50,
      "valor_pago": 87.50,
      "forma_pagamento": "DINHEIRO"
    }
  },
  {
    "id_compra": "202505170001",
    "nome_produto": "Feijão Carioca",
    "marca": "Camil",
    "categoria": "ALIMENTOS",
    "quantidade_produto": 1,
    "unidade_medida_produto": "kg",
    "quantidade": 2,
    "unidade_medida": "UN",
    "valor_unitario": 6.80,
    "valor_total": 13.60,
    "desconto": 1.00,
    "estabelecimento": {
      "nome": "Supermercado Bom Preço",
      "cnpj": "12.345.678/0001-90",
      "cidade": "São Paulo",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 17, 13, 37, 34, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": "12345",
      "codigo_nota": "0010001"
    },
    "totais": {
      "valor_total": 87.50,
      "valor_pago": 87.50,
      "forma_pagamento": "DINHEIRO"
    }
  },
  {
    "id_compra": "202505170002",
    "nome_produto": "Dipirona 500mg",
    "marca": "Neo Química",
    "categoria": "FARMÁCIA",
    "quantidade_produto": 20,
    "unidade_medida_produto": "comprimidos",
    "quantidade": 1,
    "unidade_medida": "UN",
    "valor_unitario": 12.50,
    "valor_total": 12.50,
    "desconto": None,
    "estabelecimento": {
      "nome": "Drogaria Saúde",
      "cnpj": "98.765.432/0001-10",
      "cidade": "Campinas",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 16, 15, 20, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": None,
      "codigo_nota": "0004589"
    },
    "totais": {
      "valor_total": 37.50,
      "valor_pago": 37.50,
      "forma_pagamento": "CARTAO CREDITO"
    }
  },
  {
    "id_compra": "202505170002",
    "nome_produto": "Vitamina C 500mg",
    "marca": "Vitaminlife",
    "categoria": "FARMÁCIA",
    "quantidade_produto": 60,
    "unidade_medida_produto": "comprimidos",
    "quantidade": 1,
    "unidade_medida": "UN",
    "valor_unitario": 25.00,
    "valor_total": 25.00,
    "desconto": 2.50,
    "estabelecimento": {
      "nome": "Drogaria Saúde",
      "cnpj": "98.765.432/0001-10",
      "cidade": "Campinas",
      "uf": "SP"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 16, 15, 20, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": None,
      "codigo_nota": "0004589"
    },
    "totais": {
      "valor_total": 37.50,
      "valor_pago": 37.50,
      "forma_pagamento": "CARTAO CREDITO"
    }
  },
  {
    "id_compra": "202505170003",
    "nome_produto": "Mouse Sem Fio",
    "marca": "Logitech",
    "categoria": "ELETRÔNICOS",
    "quantidade_produto": 1,
    "unidade_medida_produto": "UN",
    "quantidade": 1,
    "unidade_medida": "UN",
    "valor_unitario": 89.90,
    "valor_total": 89.90,
    "desconto": None,
    "estabelecimento": {
      "nome": "Tech Store",
      "cnpj": "55.555.555/0001-22",
      "cidade": "Rio de Janeiro",
      "uf": "RJ"
    },
    "dados_da_compra": {
      "date": datetime(2025, 5, 16, 15, 20, tzinfo=ZoneInfo("America/Sao_Paulo")),
      "numero_cupom": "98765",
      "codigo_nota": "0009876"
    },
    "totais": {
      "valor_total": 134.90,
      "valor_pago": 130.00,
      "forma_pagamento": "CARTAO DEBITO"
    }
  }
]