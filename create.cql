create table if not exists professores (id_professor int primary key, nome_professor text, departamento int);

create table if not exists grupo_tcc (id_grupo int primary key, id_professor_orientador int, nome_grupo text);

create table if not exists alunos (id_aluno int primary key, nome_aluno text, formado boolean, grupo_tcc int, nome_grupo_tcc text);

create table if not exists departamentos (id_departamento int primary key, nome_departamento text, id_chefe_departamento int);

create table if not exists cursos (id_curso int primary key, nome_curso text);

create table if not exists disciplinas (id_disciplina int primary key, nome_disciplina text, id_departamento int, id_curso int);

create table if not exists matriz_curricular (id_aluno int, id_curso int, ano int, semestre int, primary key (id_aluno, id_curso, ano));

create table if not exists historico_aluno (id_aluno int, id_disciplina int, semestre int, ano int, nota_final decimal, primary key (id_aluno, id_disciplina, semestre));

create table if not exists historico_professor (id_professor int, id_disciplina int, semestre int, ano int, primary key (id_professor, id_disciplina, semestre));
