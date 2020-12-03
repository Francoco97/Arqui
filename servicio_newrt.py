import socket
import sqlite3

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="200.14.84.235"
port =5000
sock.connect((host,port))

sock.send('00005sinitnewrt'.encode())
data = sock.recv(2010).decode()
if(data):
    print(data)

connection = sqlite3.connect('mrmuscle.sqlite')
cursor = connection.cursor()

while True:
        data = sock.recv(2010).decode()
        if(data):
            tipo = data[10]
            zona = data[11]
            intensidad = data[12]
            tiempo_total = data[13:15]

            if(zona == "2"):
                zona_cuerpo= "Piernas"
            elif(zona == "3"):
                zona_cuerpo = "Torso"
            elif(zona== "4"):
                zona_cuerpo = "Abdominales"

            if(tipo == "1"):
                if(intensidad=="1"):
                    cursor.execute("SELECT auxiliar.id FROM (SELECT * FROM Routine WHERE Routine.active_time = '20' AND Routine.rest_time = '40' AND Routine.total_time = ? AND Routine.type = '0') as auxiliar, Routine_exercise, Exercise WHERE auxiliar.id = Routine_exercise.id AND Routine_exercise.id_ex = Exercise.id AND Exercise.ex_zone = ?", (tiempo_total, zona_cuerpo))
                elif(intensidad=="2"):
                    cursor.execute("SELECT * FROM Routine, Routine_exercise, Exercise WHERE  Routine.active_time = '30' AND Routine.rest_time = '30' AND Routine.total_time = ? AND Routine.type = '0' AND Routine.id = Routine_exercise.id AND Routine_exercise.id_ex = Exercise.id AND Exercise.ex_zone = ?", (tiempo_total, zona_cuerpo))
                elif(intensidad=="3"):
                    cursor.execute("SELECT * FROM Routine, Routine_exercise, Exercise WHERE  Routine.active_time = '40' AND Routine.rest_time = '20' AND Routine.total_time = ? AND Routine.type = '0' AND Routine.id = Routine_exercise.id AND Routine_exercise.id_ex = Exercise.id AND Exercise.ex_zone = ?", (tiempo_total, zona_cuerpo))
            elif(tipo=="2"):
                    cursor.execute("SELECT * FROM Routine, Routine_exercise, Exercise WHERE  Routine.active_time = '30' AND Routine.rest_time = '30' AND Routine.total_time = ? AND Routine.type = '1' AND Routine.id = Routine_exercise.id AND Routine_exercise.id_ex = Exercise.id AND Exercise.ex_zone = ?", (tiempo_total, zona_cuerpo))

            routine = cursor.fetchall()
            print(routine)
            data = "00009newrt"
            sock.send(data.encode())

sock.close ()
conn.close()
