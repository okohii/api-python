from database.config import executar


def listar():
    print('Acesso Model: listar');
    sql = f'SELECT * FROM usuario;';
    
    print(f'Executando: ${sql}');
    return executar(sql);

