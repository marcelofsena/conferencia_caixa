import pandas as pd
import sqlite3

DB_NAME = "db.sqlite"

def importar_csv(arquivo_csv):
    # Carrega o CSV
    df = pd.read_csv(arquivo_csv)

    # Remove espaços extras nos campos
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # Conectar ao banco de dados
    conn = sqlite3.connect(DB_NAME)
    
    # Inserir os dados na tabela
    df.to_sql("tbl_swfast", conn, if_exists="append", index=False)
    
    conn.close()
    print("Importação concluída!")

# Executar importação
if __name__ == "__main__":
    importar_csv("dados.csv")
