import socket
import sqlite3


def delete_task(conn, id):
    cur = conn.cursor()
    cur.execute('DELETE FROM Routine WHERE Routine.id = ?', (id,))
    cur.execute(
        'DELETE FROM Routine_exercise WHERE Routine_exercise.id_routine = ?', (id,))
    conn.commit()


def delete_all_tasks(conn):
    cur = conn.cursor()
    cur.execute('DELETE FROM Routine')
    conn.commit()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("200.14.84.235", 5000))
sock.send('02000sinitdelrt'.encode())


try:
    con = sqlite3.connect('mrmuscle.sqlite')
except Error:
    print(Error)

while True:
    data = sock.recv(2010).decode()
    if(data):
        if data[10] == '1':
            delete_task(con, str(int(data[11:])))
        elif data[10] == '2':
            delete_all_tasks(con)
        sock.send('00020delrtLISTO'.encode())

sock.close()
conn.close()
