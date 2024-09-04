import psycopg2
from psycopg2 import sql

# Função para conectar ao banco de dados PostgreSQL
def escola_comunitaria_db():
    conn = psycopg2.connect(
        dbname="nome_do_banco",
        user="seu_usuario",
        password="sua_senha",
        host="localhost",  # ou o endereço do servidor PostgreSQL
        port="5432"
    )
    return conn

# Função para criar tabelas no banco de dados
def create_tables():
    conn = escola_comunitaria_db()
    cursor = conn.cursor()
    
    # Criar tabela para usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        tipo_usuario VARCHAR(20) CHECK (tipo_usuario IN ('aluno', 'professor', 'voluntario')) NOT NULL
    )
    ''')

    # Criar tabela para alimentos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alimentos (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        quantidade INTEGER NOT NULL,
        data_entrada DATE NOT NULL
    )
    ''')

    conn.commit()
    cursor.close()
    conn.close()

# Função para adicionar um usuário
def add_usuario(nome, tipo_usuario):
    conn = escola_comunitaria_db()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO usuarios (nome, tipo_usuario)
    VALUES (%s, %s)
    ''', (nome, tipo_usuario))

    conn.commit()
    cursor.close()
    conn.close()

# Função para adicionar um alimento
def add_alimento(nome, quantidade, data_entrada):
    conn = escola_comunitaria_db()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO alimentos (nome, quantidade, data_entrada)
    VALUES (%s, %s, %s)
    ''', (nome, quantidade, data_entrada))

    conn.commit()
    cursor.close()
    conn.close()

# Função para listar usuários
def list_usuarios():
    conn = escola_comunitaria_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return usuarios

# Função para listar alimentos
def list_alimentos():
    conn = escola_comunitaria_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM alimentos')
    alimentos = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return alimentos

# Função principal para executar o código
def main():
    create_tables()
    
    # Adicionar alguns dados de exemplo
    add_usuario('João Silva', 'voluntario')
    add_usuario('Maria Oliveira', 'professor')
    add_alimento('Arroz', 100, '2024-09-01')
    add_alimento('Feijão', 50, '2024-09-02')
    
    print('Usuários:')
    for usuario in list_usuarios():
        print(usuario)
    
    print('\nAlimentos:')
    for alimento in list_alimentos():
        print(alimento)

if __name__ == '__main__':
    main()