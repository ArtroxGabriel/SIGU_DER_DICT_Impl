CREATE OR REPLACE FUNCTION verify_capacity()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF (
        (SELECT capacidade_maxima
         FROM turma
         WHERE id = NEW.turma_id
        ) <= 
        (SELECT COUNT(*)
         FROM aluno_turma
         WHERE turma_id = NEW.turma_id
        )
    ) THEN
        RAISE EXCEPTION 'Não é possível adicionar estudantes a turma %: capacidade excedida.', NEW.turma_id;
    END IF;
	
    RETURN NEW;
END;
$$;

CREATE TRIGGER avoid_overflow_capacity
BEFORE INSERT
ON aluno_turma
FOR EACH ROW
EXECUTE FUNCTION verify_capacity();


CREATE OR REPLACE FUNCTION limit_courses_per_student()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF (
        (SELECT COUNT(*)
         FROM aluno_turma
         WHERE aluno_turma.aluno_id = NEW.aluno_id
        ) >= 4
    ) THEN
        RAISE EXCEPTION 'Estudante % não pode estar matriculado em mais de 4 turmas.', NEW.aluno_id;
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER courses_limitation
BEFORE INSERT
ON aluno_turma
FOR EACH ROW
EXECUTE FUNCTION limit_courses_per_student();
