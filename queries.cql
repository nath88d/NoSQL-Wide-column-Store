// Histórico do Aluno

SELECT * FROM historico_aluno WHERE id_aluno = 8;

//Histórico do Professor

SELECT id_disciplina, semestre, ano FROM historico_professor WHERE id_professor = 1;

//Alunos Formados em Determinado Semestre/Ano
//OBS: Substituir o "?" pelo id_aluno desejado para descobrir o nome do aluno

SELECT id_aluno FROM matriz_curricular WHERE semestre = 8 AND ano = 2016 ALLOW FILTERING;
SELECT id_aluno, nome_aluno FROM alunos WHERE id_aluno = ? AND formado = true;

//Lista de Professores Chefes de Departamento
//OBS: Substituir o "?" pelo id_professor desejado para descobrir o nome do professor

SELECT id_chefe_departamento, nome_departamento FROM departamentos;
SELECT nome_professor FROM professores WHERE id_professor = ?;


// Alunos que Formam Grupo de TCC com o Nome do Orientador
//OBS: Substituir o "?" pelo id_grupo, grupo_tcc ou id_professor desejados

SELECT id_grupo, id_professor_orientador, nome_grupo FROM grupo_tcc WHERE id_grupo = ?;
SELECT id_aluno, nome_aluno FROM alunos WHERE grupo_tcc = ?;
SELECT nome_professor FROM professores WHERE id_professor = ?;


