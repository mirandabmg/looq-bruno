#obs: O ideal seria criar uma venv para separar e instalar as dependências, ou estruturar um projeto com todos os scripts utilizados, se este case fosse um projeto inteiro.

import pandas as pd
from sqlalchemy import create_engine, text

# conexão com banco
engine = create_engine(
    "mysql+pymysql://looqbox-challenge:looq-challenge@35.199.115.174:3306/lookbox_challenge"
)

# função principal
def retrieve_data(product_code=None, store_code=None, date=None):

    # query base
    query = """
    SELECT *
    FROM DATA_PRODUCT_SALES
    WHERE 1=1
    """

    # parâmetros da query
    params = {}

    # filtro de produto
    if product_code is not None:
        query += " AND PRODUCT_CODE = :product_code"
        params["product_code"] = product_code

    # filtro de loja
    if store_code is not None:
        query += " AND STORE_CODE = :store_code"
        params["store_code"] = store_code

    # filtro de data
    if date is not None:

        if not isinstance(date, list):
            raise ValueError("date must be a list")

        if len(date) != 2:
            raise ValueError("date must contain start and end date")

        query += " AND DATE BETWEEN :start_date AND :end_date"

        params["start_date"] = date[0]
        params["end_date"] = date[1]

    # debug simples
    print(query)
    print(params)

    # execução da query
    df = pd.read_sql_query(
        text(query),
        con=engine,
        params=params
    )

    return df
