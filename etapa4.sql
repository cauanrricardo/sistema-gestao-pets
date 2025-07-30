--viwe 01
CREATE VIEW view_consultas_detalhadas AS
SELECT 
    c.id_consulta,
    p.nome_pet,
    p.raca,
    p.sexo,
    t.nome AS tutor,
    pr.nome_profissional AS profissional,
    pr.especialidade,
    c.data AS data_consulta,
    c.hora AS hora_consulta,
    c.diagnostico,
    c.descricao,
    c.prescricao,
    cl.nome_clinica AS clinica
FROM Consulta c
JOIN Pet p ON c.id_pet = p.id_pet
JOIN Tutor t ON p.id_tutor = t.id_tutor
JOIN Profissional pr ON c.id_profissional = pr.id_profissional
LEFT JOIN Trabalha_Em te ON pr.id_profissional = te.id_profissional
LEFT JOIN Clinica cl ON te.id_clinica = cl.id_clinica;

SELECT * FROM view_consultas_detalhadas;

--view 02
CREATE VIEW vw_atividades_profissionais AS
SELECT 
    pr.id_profissional,
    pr.nome_profissional,
    pr.especialidade,
    pr.telefone,
    
    cl.nome_clinica,
    te.carga_horaria,

    COUNT(c.id_consulta) AS total_consultas_realizadas

FROM Profissional pr
JOIN Trabalha_Em te ON pr.id_profissional = te.id_profissional
JOIN Clinica cl ON cl.id_clinica = te.id_clinica
LEFT JOIN Consulta c ON c.id_profissional = pr.id_profissional

GROUP BY 
    pr.id_profissional,
    pr.nome_profissional,
    pr.especialidade,
    pr.telefone,
    cl.nome_clinica,
    te.carga_horaria;

SELECT * FROM vw_atividades_profissionais;

-- Usuário administrador
CREATE USER administrador_vet WITH PASSWORD '12345678910';

-- Usuário somente leitura
CREATE USER recepcionista_vet WITH PASSWORD '10987654321';

GRANT SELECT ON ALL TABLES IN SCHEMA public TO administrador_vet;
GRANT INSERT ON ALL TABLES IN SCHEMA public TO administrador_vet;
GRANT UPDATE ON ALL TABLES IN SCHEMA public TO administrador_vet;
GRANT DELETE ON ALL TABLES IN SCHEMA public TO administrador_vet;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO recepcionista_vet;
