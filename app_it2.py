import psycopg2

# Подключение к базе данных
try:
    conn = psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="postgres",
        host="db",  # Имя сервиса из docker-compose.yml
        port="5432"
    )
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            department VARCHAR(100)
        );
    """)

    # Наполнение таблицы данными
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s);",
                   ("Alice", 30, "Engineering"))
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s);",
                   ("Bob", 25, "Marketing"))

    # Сохранение изменений
    conn.commit()

    # Вывод данных из таблицы
    cursor.execute("SELECT * FROM employees;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print(f"Ошибка подключения к базе данных: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()
