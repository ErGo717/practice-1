CREATE OR REPLACE PROCEDURE upsert_contact(
    p_username VARCHAR(100),
    p_phone VARCHAR(20)
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_username) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE username = p_username;
    ELSE
        INSERT INTO phonebook(username, phone)
        VALUES (p_username, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE bulk_upsert_contacts(
    p_usernames TEXT[],
    p_phones TEXT[],
    INOUT bad_rows TEXT[] DEFAULT ARRAY[]::TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    v_username TEXT;
    v_phone TEXT;
    v_len INT;
BEGIN
    bad_rows := ARRAY[]::TEXT[];

    v_len := LEAST(
        COALESCE(array_length(p_usernames, 1), 0),
        COALESCE(array_length(p_phones, 1), 0)
    );

    FOR i IN 1..v_len LOOP
        v_username := trim(p_usernames[i]);
        v_phone := trim(p_phones[i]);

        IF v_username = '' OR v_phone !~ '^\+?[0-9]{10,15}$' THEN
            bad_rows := array_append(
                bad_rows,
                format('%s | %s', v_username, v_phone)
            );
        ELSE
            BEGIN
                IF EXISTS (SELECT 1 FROM phonebook WHERE username = v_username) THEN
                    UPDATE phonebook
                    SET phone = v_phone
                    WHERE username = v_username;
                ELSE
                    INSERT INTO phonebook(username, phone)
                    VALUES (v_username, v_phone);
                END IF;
            EXCEPTION
                WHEN unique_violation THEN
                    bad_rows := array_append(
                        bad_rows,
                        format('%s | %s (duplicate)', v_username, v_phone)
                    );
            END;
        END IF;
    END LOOP;

    IF COALESCE(array_length(p_usernames, 1), 0)
       <> COALESCE(array_length(p_phones, 1), 0) THEN
        bad_rows := array_append(bad_rows, 'Input arrays have different lengths');
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact_proc(
    p_username VARCHAR(100) DEFAULT NULL,
    p_phone VARCHAR(20) DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_username IS NOT NULL THEN
        DELETE FROM phonebook WHERE username = p_username;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = p_phone;
    ELSE
        RAISE EXCEPTION 'Provide username or phone';
    END IF;
END;
$$;