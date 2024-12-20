import names
import random as rand
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

# This secure connect bundle is autogenerated when you download your SCB, 
# if yours is different update the file name below
cloud_config= {
  'secure_connect_bundle': 'secure-connect-<NOME_DO_SEU_KEYSPACE>.zip'
}

# This token JSON file is autogenerated when you download your token, 
# if yours is different update the file name below
with open("<NOME_DO_SEU_BANCO>-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

# Solicitar entradas
num_de_pessoas = int(input("Insira o numero de pessoas para inserir no banco: "))
depart = [453, 654, 236, 735]
formado = [True, False]

session.execute("use <NOME_DO_SEU_KEYSPACE>;")


def gerar(query):
    try:
        result = session.execute(query)
        print(f"Sucesso: {result}")
    except Exception as e:
        print(f"Erro: {e} na tabela {query}")

def delete_all_data_from_table(tabela):
    try:
        query = f"TRUNCATE {tabela};"
        session.execute(query)
        print(f"Todos os dados da tabela {tabela} foram deletados com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar dados da tabela {tabela}: {e}")

# Lista das tabelas para limpar
tabelas = [
    'professores', 
    'grupo_tcc', 
    'alunos', 
    'departamentos', 
    'cursos', 
    'disciplinas', 
    'matriz_curricular', 
    'historico_aluno', 
    'historico_professor'
]

# Deletar todos os dados de todas as tabelas
for tabela in tabelas:
    delete_all_data_from_table(tabela)

# Inserir departamentos
departamentos = [
    {"id_departamento":453, "nome_departamento":"Computacao", "id_chefe_departamento":0},
    {"id_departamento":654, "nome_departamento":"Engenharia", "id_chefe_departamento":0},
    {"id_departamento":236, "nome_departamento":"Administracao", "id_chefe_departamento":0},
    {"id_departamento":735, "nome_departamento":"Economia", "id_chefe_departamento":0}
]

# Função para inserir departamentos
for departamento in departamentos:
    query = """
    INSERT INTO departamentos (id_departamento, nome_departamento, id_chefe_departamento)
    VALUES (%d, '%s', %d);
    """%(departamento["id_departamento"],departamento["nome_departamento"],departamento["id_chefe_departamento"])
    gerar(query)

# Inserir cursos
cursos = [
    {"id_curso": 0, "nome_curso": "Administração de Empresas"},
    {"id_curso": 1, "nome_curso": "Gestão de Recursos Humanos"},
    {"id_curso": 2, "nome_curso": "Engenharia Civil"},
    {"id_curso": 3, "nome_curso": "Engenharia Elétrica"},
    {"id_curso": 4, "nome_curso": "Ciência da Computação"},
    {"id_curso": 5, "nome_curso": "Engenharia de Software"},
    {"id_curso": 6, "nome_curso": "Economia"},
    {"id_curso": 7, "nome_curso": "Finanças"}
]

# Função para inserir cursos
for curso in cursos:
    query = """
    INSERT INTO cursos (ID_curso, Nome_curso) 
    VALUES (%d, '%s');
    """ % (curso["id_curso"], curso["nome_curso"])
    gerar(query)

# Inserir disciplinas
disciplinas = [
    {"id": 0, "nome_disciplina": "Comp. Sci.", "id_departamento": 453, "semestre": 4},
    {"id": 1, "nome_disciplina": "Finance", "id_departamento": 654, "semestre": 7},
    {"id": 2, "nome_disciplina": "Eng. eletrica", "id_departamento": 236, "semestre": 3},
    {"id": 3, "nome_disciplina": "Physics", "id_departamento": 735, "semestre": 4},
    {"id": 4, "nome_disciplina": "Desenvolvimento Web", "id_departamento": 453, "semestre": 4},
    {"id": 5, "nome_disciplina": "Mercado de Capitais", "id_departamento": 654, "semestre": 7},
    {"id": 6, "nome_disciplina": "Eletromagnetismo", "id_departamento": 236, "semestre": 3},
    {"id": 7, "nome_disciplina": "Astrofísica", "id_departamento": 735, "semestre": 4},
    {"id": 8, "nome_disciplina": "Gestão de Recursos Humanos", "id_departamento": 453, "semestre": 0},
    {"id": 9, "nome_disciplina": "Segurança da Informação", "id_departamento": 654, "semestre": 7},
    {"id": 10, "nome_disciplina": "Gestão de Riscos", "id_departamento": 236, "semestre": 3},
    {"id": 11, "nome_disciplina": "Energias Renováveis", "id_departamento": 735, "semestre": 4},
    {"id": 12, "nome_disciplina": "Mecânica Quântica", "id_departamento": 453, "semestre": 4},
    {"id": 13, "nome_disciplina": "Marketing Estratégico", "id_departamento": 654, "semestre": 7},
    {"id": 14, "nome_disciplina": "Big Data Analytics", "id_departamento": 236, "semestre": 3},
    {"id": 15, "nome_disciplina": "Derivativos Financeiros", "id_departamento": 735, "semestre": 7},
    {"id": 16, "nome_disciplina": "Eletrônica de Potência", "id_departamento": 453, "semestre": 3},
    {"id": 17, "nome_disciplina": "Física Nuclear", "id_departamento": 654, "semestre": 4},
    {"id": 18, "nome_disciplina": "Empreendedorismo", "id_departamento": 236, "semestre": 0},
    {"id": 19, "nome_disciplina": "Aprendizado de Máquina", "id_departamento": 735, "semestre": 4},
    {"id": 20, "nome_disciplina": "Finanças Corporativas", "id_departamento": 453, "semestre": 7},
    {"id": 21, "nome_disciplina": "Telecomunicações", "id_departamento": 654, "semestre": 5},
    {"id": 22, "nome_disciplina": "Óptica Avançada", "id_departamento": 236, "semestre": 3},
    {"id": 23, "nome_disciplina": "Gestão da Qualidade", "id_departamento": 735, "semestre": 0}
]

for disciplina in disciplinas:
    query = """
    INSERT INTO disciplinas (id_disciplina, nome_disciplina, id_departamento, semestre) 
    VALUES (%d, '%s', %d, %d);
    """ % (disciplina["id"], disciplina["nome_disciplina"], disciplina["id_departamento"], disciplina["semestre"])
    gerar(query)

# Inserir Professores
num = 0
for i in range(num_de_pessoas):  # Inserir professores
    query = """
    INSERT INTO professores (id_professor, nome_professor, departamento)
    VALUES (%d, '%s', %d);
    """ % (num, names.get_full_name(), depart[rand.randint(0, 3)])
    gerar(query)
    num += 1

# Inserir Alunos
num = 0
for i in range(num_de_pessoas):  # Inserir alunos
    query = """
    INSERT INTO alunos (id_aluno, nome_aluno, formado, grupo_tcc)
    VALUES (%d, '%s', %s, %d);
    """ % (num, names.get_full_name(), formado[rand.randint(0, 1)], 0)
    gerar(query)
    num += 1

# Inserir Histórico de Professores
num = 0
for i in range(num_de_pessoas):  # Inserir histórico de professores
    for h in range(1, 4):
        query = """
        INSERT INTO historico_professor (id_professor, id_disciplina, semestre, ano)
        VALUES (%d, %d, %d, %d);
        """ % (num, rand.randint(0, 23), rand.randint(1, 8), rand.randint(2000, 2024))
        gerar(query)
    num += 1

# Inserir Grupo TCC
num = 0
for i in range(round(0.2 * num_de_pessoas)):  # Inserir grupo TCC
    query = """
    INSERT INTO grupo_tcc (id_grupo, id_professor_orientador)
    VALUES (%d, %d);
    """ % (num, rand.randint(0, num_de_pessoas - 1))
    gerar(query)
    num += 1
    
    
    
    
# Inserir histórico do aluno
for i in range(num_de_pessoas):
    nota = rand.uniform(0, 10)
    curso = rand.randint(0, 7)
    data_inicial = rand.randint(2000, 2024)
    sem_inicial = rand.randint(1, 8)

    # Inserir na matriz curricular
    query = """
    INSERT INTO matriz_curricular (id_aluno, id_curso, ano, semestre)
    VALUES (%d, %d, %d, %d);
    """ % (i, curso, data_inicial, 8)
    gerar(query)

    
    semestre = 0
    disciplina_percorrida = []
    for m in range(0,rand.randint(1,7)):
        semestre += 1
        disc = rand.randint(0,(len(disciplinas)-1))
        if disc not in disciplina_percorrida:
            query = """
                INSERT INTO historico_aluno (id_aluno, id_disciplina, semestre, ano, nota_final)
                VALUES (%d, %d, %d, %d, %.2f);
                """ % (i, disciplinas[disc]["id"], semestre, data_inicial, round(nota, 2))
            # print(query)
            gerar(query)
            data_inicial += 1


        # Atualizar estado de formado
        if nota >= 5 and sem_inicial == 8:
            grupo = rand.randint(0, round(0.2 * num_de_pessoas))
            gerar("""
        UPDATE alunos
        SET formado = true, grupo_tcc = %d
        WHERE id_aluno = %d;
        """ % (grupo, i))
        else:
            gerar(query = """
        UPDATE alunos
        SET formado = false
        WHERE id_aluno = %d;
        """ % (i))
    
    
    
    

departamentos = [
    {"id_departamento": 453},
    {"id_departamento": 654},
    {"id_departamento": 236},
    {"id_departamento": 735}
]

# Atualizar chefes de departamentos
for departamento in departamentos:
    chefe_id = rand.randint(0, num_de_pessoas - 1)
    query = """
    UPDATE departamentos
    SET id_chefe_departamento = %d
    WHERE id_departamento = %d;
    """ % (chefe_id, departamento["id_departamento"])
    gerar(query)

print("\nDados inseridos com sucesso!")
