#!/usr/bin/env python
# -- coding: utf-8 --
import socket
import sqlite3


def DB(conn, cur):
    cur.execute(
        'CREATE TABLE Routine (id INTEGER PRIMARY KEY, active_time INTEGER, rest_time INTEGER, total_time INTEGER, type int)')
    cur.execute(
        'CREATE TABLE Exercise (id INTEGER PRIMARY KEY, name VARCHAR , detail VARCHAR, type INTEGER, ex_zone VARCHAR, level int)')
    cur.execute(
        'CREATE TABLE Routine_exercise (id INTEGER PRIMARY KEY, id_routine INTEGER, id_ex INTEGER, minute INTEGER, FOREIGN KEY(id_routine) REFERENCES Routine(id), FOREIGN KEY(id_ex) REFERENCES Exercise(id))')

    #MUSCULATURA - Piernas
    # nivel 1
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Puente","Recuestate boca arriba con tus rodillas flexionadas. Contrae tus musculos abdominales. Eleva la cadera del suelo hasta que la cadera esté en línea con las rodillas y los hombros", 1, "Piernas", 1)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Sentadilla","Flexiona las rodillas y baja el cuerpo manteniendo la verticalidad, luego regresa a la posicion erguida", 1, "Piernas", 1)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Peso muerto libre","Colocate de pie con las piernas separadas a la anchura de los hombros, flexiona las rodillas manteniendo la espalda totalmente recta. Empieza a descender utilizando las caderas", 1, "Piernas", 1)')

    # nivel 2
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Lunge","Este de pie con las manos en puño apoyadas en la cintura y las piernas ligeramente separadas. Luego de un paso hacia delante", 1, "Piernas", 2)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Sentadilla sumo","Separa las piernas para que los talones estén con una distancia amplia. Baja hasta que las caderas esten en la misma linea, a la misma altura que las rodillas", 1, "Piernas", 2)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Puente con una pierna","Acuestese boca arriba con los brazos a los lados, las rodillas dobladas y los pies apoyados en el suelo. Levante una pierna y levante las caderas tan alto como pueda. Baja las caderas, repite y luego cambia de pierna", 1, "Piernas", 2)')

    # nivel 3
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Sentadilla con salto","Este de pie con los pies juntos, y coloca las manos sobre los muslos. Flexiona las rodillas, salta y separa los pies en pleno salto. Déjate caer con los pies separados a una distancia mayor que los hombros, bajando hasta quedar en posicion de sentadilla", 1, "Piernas", 3)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Peso muerto con una pierna","Ponte de pie apoyado sobre una sola pierna. Inclina el torso hacia el suelo con la espalda recta manteniendo el equilibrio.", 1, "Piernas", 3)')

    #MUSCULATURA - Torso
    # nivel 1
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Flexion de rodillas","Ponte de rodillas y apoya las manos en el suelo en línea con los hombros. Manten los codos pegados al tronco y flexionalos para bajar el cuerpo hasta que el pecho casi toque el suelo, luego sube", 1, "Torso", 1)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Plancha brazos estirados","Apoyarse en el suelo con manos y pies estirando codos y rodillas, mantener.", 1, "Torso", 1)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Superman","Tensa tus musculos abdominales para mantener tu torso estable, luego levanta del suelo unas cuantas pulgadas los brazos, la parte superior del pecho y las piernas simultaneamente. Manten esta posición un momento antes de volver a bajar suavemente tus brazos y piernas", 1, "Torso", 1)')

    # nivel 2
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Flexion normal","Acuestate mirando hacia el suelo, apoyandote unicamente con la punta de los pies y las palmas de las manos. Flexiona los brazos manteniendo en todo momento los codos cerca del cuerpo hasta rozar el suelo con el pecho sin llegar a apoyarse en el. Vuelve a la posicion inicial estirando los brazos", 1, "Torso", 2)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Superman nadando","Tumbate boca abajo en una superficie comoda, extiende pies y brazos y elevalos levemente para que no toquen el suelo, a continuación pasa a elevar pies y brazos simultaneamente (como al nadar)", 1, "Torso", 2)')

    # nivel 3
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Plancha lateral","En posicion de plancha, con los brazos estirados, gira el tronco de tal manera que el cuerpo quede alineado en una plancha lateral", 1, "Torso", 3)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Plancha invertida","Sientate en el suelo con las piernas juntas. Recuestate hacia atrás formando un ángulo de 45 grados entre el suelo y el tronco, apoyando las manos en el suelo con los brazos perpendiculares al suelo. Levanta la pelvis hacia arriba despegando el cuerpo del suelo y contrayendo los gluteos hasta formar una linea recta con el cuerpo. Debes mantener los talones apoyados en el suelo.", 1, "Torso", 3)')

    #MUSCULATURA - Abdominales
    # nivel 1
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Plancha sobre antebrazos","Coloquese boca abajo. Extienda las piernas detras de usted. Aguante su peso con los dedos de los pies y los antebrazos. Sus antebrazos deben estar en paralelo entre ellos. Apriete sus musculos abdominales y oblicuos", 1, "Abdominales", 1)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Posicion concava 1","Acostarse en el suelo con las rodillas flexionadas sobre las caderas y levantar los brazos estirados apoyando los lumbrares en el piso, mantener.", 1, "Abdominales", 1)')

    # nivel 2
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Mountain climber","Tumbate boca abajo en el suelo apoyando las manos con los dedos dirigidos hacia el frente a la anchura de los hombros. Luego comienza el movimiento consistente en llevar de manera alterna las rodillas hacia el codo opuesto", 1, "Abdominales", 2)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Posicion concava 2","Acostarse en el suelo con las piernas estiradas y los brazos estirados a los costados del torso, levantar las cuatro extremidades apoyando solo los lumbares en el piso, mantener.", 1, "Abdominales", 2)')

    # nivel 3
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Plancha sobre antebrazos","Coloquese boca abajo. Extienda las piernas detrás de usted. Aguante su peso con los dedos de los pies y los antebrazos. Sus antebrazos deben estar en paralelo entre ellos. Apriete sus musculos abdominales y oblicuos", 1, "Abdominales", 3)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Posicion concava 3","Acostarse en el suelo con las piernas estiradas y los brazos estirados sobre la cabeza, levantar las cuatro extremidades apoyando solo los lumbares en el piso, mantener.", 1, "Abdominales", 3)')

    #CARDIO - Torso
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Burpees","Comenzar parado con piernas abiertas a lo ancho de los hombros, agacharse apoyando las manos en el piso, acostarse en el piso, levantarse a posicion agachada, pararse dando un salto y aplaudir las manos sobre la cabeza.", 0, "Torso", 0)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Mountain climber","Tumbate boca abajo en el suelo apoyando las manos con los dedos dirigidos hacia el frente a la anchura de los hombros. Luego comienza el movimiento consistente en llevar de manera alterna las rodillas hacia el pecho.", 0, "Torso", 0)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Caminar hacia pies","Apoyarse en el suelo con manos y pies estirando codos y rodillas, caminar con las manos hacia los pies, no es necesario tener los pies estirados al finalizar el movimiento.", 0, "Torso", 0)')

    #CARDIO - Piernas
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Sentadillas sin salto","Coloca las manos en el suelo y manten la cabeza erguida. Desplaza las piernas hacia atras con los pies juntos y haz una flexion de pecho, para luego volver a la posición inicial", 0, "Piernas", 0)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Sentadillas con salto","Coloca las manos en el suelo y manten la cabeza erguida. Desplaza las piernas hacia atras con los pies juntos y haz una flexion de pecho, para luego volver a la posición inicial y saltar", 0, "Piernas", 0)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Lunges sin salto","Comienza en posicion de zancada, con un pie al frente y el otro atras, las manos en las caderas, el torso derecho y las rodillas flexionadas formando un angulo de 90. Sin levantarte, cambia tus piernas de posicion", 0, "Piernas", 0)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Lunges con salto","Comienza en posicion de zancada, con un pie al frente y el otro atras, las manos en las caderas, el torso derecho y las rodillas flexionadas formando un angulo de 90. Abalanzate con fuerza desde el suelo, saltando y cambiando la posicion de las piernas a mitad de salto", 0, "Piernas", 0)')

    #CARDIO - Abdominales
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Mountain climber","Tumbate boca abajo en el suelo apoyando las manos con los dedos dirigidos hacia el frente a la anchura de los hombros. Luego comienza el movimiento consistente en llevar de manera alterna las rodillas hacia el pecho.", 0, "Abdominales", 0)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Caminar hacia pies","Apoyarse en el suelo con manos y pies estirando codos y rodillas, caminar con las manos hacia los pies, no es necesario tener los pies estirados al finalizar el movimiento.", 0, "Abdominales", 0)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Rodillazo al frente","Colocate de pie con un pie situado ligeramente detrás de ti. Manten el peso sobre el pie delantero y levanta la rodilla trasera frente a ti, repite de manera alterna.", 0, "Abdominales", 0)')

    #CARDIO - Otros
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Jumping Jacks","De pie con las piernas juntas y los brazos pegados a los muslos, da un salto manteniendo la espalda recta y las piernas separadas a la anchura de los hombros. Al juntar las piernas, tus brazos han de tocar los muslos", 0, "Otros", 0)')
    cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Skipping lateral","Repetidamente eleva las rodillas por encima de la cintura manteniendo la cadera en una posicion elevada", 0, "Otros", 0)')

    conn.commit()

    conn.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "200.14.84.235"
port = 5000
sock.connect((host, port))

sock.send('02000sinitdbini'.encode())
data = sock.recv(2010).decode()
if(data):
    print(data)

connection = sqlite3.connect('mrmuscle.sqlite')
cursor = connection.cursor()

try:
    cursor.execute("SELECT EXISTS (SELECT * FROM Exercise)")
    print("PUEDE INICIAR")
except:
    DB(connection, cursor)
    print("PUEDE INICIAR")
