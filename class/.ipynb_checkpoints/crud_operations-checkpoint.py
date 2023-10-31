import psycopg2


def execute_query(conn, query, parameters=None):
    try:
        cur = conn.cursor()
        if parameters:
            cur.execute(query, parameters)
        else:
            cur.execute(query)
        conn.commit()
        cur.close()
    except psycopg2.Error as e:
        print("Error al ejecutar la consulta:", e)


def select_query(conn, query, parameters=None):
    try:
        cur = conn.cursor()
        if parameters:
            cur.execute(query, parameters)
        else:
            cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    except psycopg2.Error as e:
        print("Error al ejecutar la consulta:", e)
        return []


def insert_record(conn, table, data):
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s' for _ in data])
    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    execute_query(conn, query, list(data.values()))


def update_record(conn, table, data, where_clause):
    set_values = ', '.join([f"{key} = %s" for key in data])
    query = f"UPDATE {table} SET {set_values} WHERE {where_clause}"
    execute_query(conn, query, list(data.values()))


def delete_record(conn, table, where_clause):
    query = f"DELETE FROM {table} WHERE {where_clause}"
    execute_query(conn, query)
