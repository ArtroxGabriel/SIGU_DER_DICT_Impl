CREATE OR REPLACE PROCEDURE inc_semestre(target_semestre INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE aluno
    SET semestre = semestre + 1
    WHERE semestre = target_semestre;
END;
$$;