import sqlite3

DB="reports.db"


def init_db():

    conn=sqlite3.connect(DB)
    cur=conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        venue TEXT,
        start_time TEXT,
        end_time TEXT,
        attendance INTEGER,
        income INTEGER,
        expenditure INTEGER,
        profit_loss INTEGER,
        drive_link TEXT,
        avenue TEXT,
        project_level TEXT,
        project_hours TEXT,
        man_hours TEXT,
        created_by TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_report(data):

    conn=sqlite3.connect(DB)
    cur=conn.cursor()

    cur.execute("""
    INSERT INTO reports(
    title,venue,start_time,end_time,
    attendance,income,expenditure,profit_loss,
    drive_link,avenue,project_level,
    project_hours,man_hours,created_by)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,data)

    conn.commit()
    conn.close()


def load_reports():

    conn=sqlite3.connect(DB)
    cur=conn.cursor()

    rows=cur.execute("SELECT * FROM reports ORDER BY id DESC").fetchall()

    conn.close()

    return rows