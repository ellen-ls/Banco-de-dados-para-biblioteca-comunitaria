-- Tabela de usuários com CHECK constraint
CREATE TABLE Usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_usuario VARCHAR(50) NOT NULL,
    CONSTRAINT tipo_usuario_check CHECK (tipo_usuario IN ('aluno', 'professor', 'voluntario'))
);

-- Tabela de atividades
CREATE TABLE Atividades (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_atividade DATE NOT NULL,
    local VARCHAR(255) NOT NULL,
    horario TIME NOT NULL
);

-- Tabela de materiais
CREATE TABLE Materiais (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    quantidade INT DEFAULT 0,
    data_aquisicao DATE
);

-- Tabela de participações
CREATE TABLE Participacoes (
    id SERIAL PRIMARY KEY,
    usuario_id INT,
    atividade_id INT,
    data_participacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id),
    FOREIGN KEY (atividade_id) REFERENCES Atividades(id)
);

-- Inserção de dados exemplo na tabela de usuários
INSERT INTO Usuarios (nome, email, tipo_usuario) VALUES 
('João da Silva', 'joao.silva@example.com', 'aluno'),
('Maria Oliveira', 'maria.oliveira@example.com', 'professor'),
('Carlos Souza', 'carlos.souza@example.com', 'voluntario');

-- Inserção de dados exemplo na tabela de atividades
INSERT INTO Atividades (nome, descricao, data_atividade, local, horario) VALUES 
('Oficina de Artes', 'Oficina para desenvolver habilidades artísticas.', '2024-09-10', 'Sala de Artes', '14:00:00'),
('Palestra sobre Sustentabilidade', 'Palestra sobre práticas sustentáveis no cotidiano.', '2024-09-15', 'Auditório', '10:00:00');

-- Inserção de dados exemplo na tabela de materiais
INSERT INTO Materiais (nome, descricao, quantidade, data_aquisicao) VALUES 
('Tintas Acrílicas', 'Tintas para uso em oficinas de arte.', 50, '2024-08-20'),
('Projetor', 'Projetor para apresentações e palestras.', 2, '2024-08-15');

-- Inserção de dados exemplo na tabela de participações
INSERT INTO Participacoes (usuario_id, atividade_id) VALUES 
(1, 1),
(2, 2),
(3, 1);