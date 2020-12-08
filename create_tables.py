import sqlite3

sql_exercise_table = """CREATE TABLE exercise (id INTEGER AUTO_INCREMENT NOT NULL, name TEXT, detail TEXT, type INTEGER, ex_zone TEXT, level INTEGER, PRIMARY KEY (id));"""
sql_routine_table = """CREATE TABLE routine (id INTEGER AUTO_INCREMENT NOT NULL, active_time INTEGER, type INTEGER, PRIMARY KEY (id));"""
sql_routine_exercise_table = """CREATE TABLE routine_exercise (id INTEGER AUTO_INCREMENT NOT NULL, id_routine INTEGER, id_exercise INTEGER, PRIMARY KEY (id), FOREIGN KEY (id_routine) REFERENCES routine(id), FOREIGN KEY (id_exercise) REFERENCES exercise(id));"""

sql_insert_exercises_piernas = """
INSERT INTO exercise (name, type, detail, ex_zone, level) values ("Puente de glúteos", "Acostarse en el piso, apoyar pies en el piso con las caderas apoyadas en el suelo, subir cadera apretando los glúteos, repetir.", 1, "piernas", 1);
INSERT INTO exercise (name, type, detail, ex_zone, level) values ("Sentadilla", "Pararse con las piernas abiertas a lo ancho de los hombros, apuntar pies hacia afuera y luego intentar sentarse en el piso, repetir.", 1, "piernas", 1);
INSERT INTO exercise (name, type, detail, ex_zone, level) values ("Peso muerto libre", "Pararse comodamente para luego agacharse con las espalda recta hasta tocar el piso con las manos, repetir.", 1, "piernas", 1);
INSERT INTO exercise (name, type, detail, ex_zone, level) values ("Estocada", "Pararse comodamente para luego llevar una rodilla al piso flexionando y manteniendo el equilibrio con la pierna contraria, alterar y repetir.", 1, "piernas", 2);
INSERT INTO exercise (name, type, detail, ex_zone, level) values ("Sentadilla sumo", "Pararse con las piernas muy abiertas, como un sumo, apuntar pies hacia afuera y luego intentar sentarse en el piso, repetir.", 1, "piernas", 2);
INSERT INTO exercise (name, type, detail, ex_zone, level) values ("Puente de glúteos con una pierna", "Acostarse en el piso, apoyar un pie en el piso con las caderas apoyadas en el suelo, subir cadera apretando los glúteos, repetir.", 1, "piernas", 2);
INSERT INTO exercise (name, type, detail, ex_zone, level) values ("Sentadilla con salto", Pararse con las piernas abiertas a lo ancho de las caderas, apuntar pies hacia afuera, intentar sentarse en el piso, subir tan fuerte que se levantan los pies del suelo, repetir.", 1, "piernas", 3);
INSERT INTO exercise (name, type, detail, ex_zone, level) values ("Peso muerto con una pierna", "Pararse comodamente en una pierna para luego agacharse con las espalda recta hasta tocar el piso con las manos, repetir.", 1, "piernas", 3);
"""

sql_insert_exercises_torso = """
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Flexión de brazos sobre rodillas", "Estirar los brazos y apoyarse en el suelo con las manos y rodillas,  bajar el pecho flexionando los codos con el tronco recto, repetir.", 1, "torso", 1);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Plancha brazos estirados", "Apoyarse en el suelo con manos y pies estirando codos y rodillas, mantener.", 1, torso, 1);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Superman", "Acostarse boca abajo en el piso, situar brazos estirados sobre la cabeza, levantar simultaneamente brazos y piernas apretando la espalda y glúteos, repetir.", 1, "torso", 1);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Flexión de brazos", "Apoyarse en el suelo con manos y pies estirando codos y rodillas,  bajar el pecho flexionando los codos con el tronco recto, repetir.", 1, "torso", 2);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Superman nadador", "Acostarse boca abajo en el piso, situar brazos estirados sobre la cabeza, mantener levantados brazos y piernas apretando la espalda y glúteos, llevar brazos hacia los costados del torso, repetir.", 1, "torso", 2);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Plancha lateral", "De costado apoyarse en el suelo con una mano y pies jutnos estirando codos y rodillas, mantener.", 1, "torso", 3);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Plancha invertida", "Mirando hacia el cielo, apoyarse en el suelo con manos y pies estirando codos y rodillas, mantener el pecho abierto y glúteos lo más alto posible, mantener.", 1, "torso", 3);
"""

sql_insert_exercises_abs = """
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Plancha sobre antebrazos nivel 1", "Apoyarse en el suelo con los antebrazos y pies estirando rodillas, mantener", 1, "abdominales", 1);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Posición cóncava nivel 1", "Acostarse en el suelo con las rodillas flexionadas sobre las caderas y levantar los brazos estirados apoyando los lumbraes en el piso, mantener.", 1, "abdominales", 1);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Escalador de montaña", "Apoyarse en el suelo con manos y pies estirando codos y rodillas, llevar una rodilla al pecho mientras el otro pie se mantiene en el piso, alternar y repetir.", 1, "abdominales", 2);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Posición cóncava nivel 2", "Acostarse en el suelo con las piernas estiradas y los brazos estirados a los costados del torso, levantar las cuatro extremidades apoyando solo los lumbares en el piso, mantener.", 1, "abdominales", 2);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Plancha sobre antebrazos nivel 2", "Apoyarse en el suelo con los antebrazos y pies estirando rodillas, posicionar los antebrazos lo más lejos que se pueda de ti ,mantener.", 1, "abdominales", 3);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Posición cóncava nivel 3", "Acostarse en el suelo con las piernas estiradas y los brazos estirados sobre la cabeza, levantar las cuatro extremidades apoyando solo los lumbares en el piso, mantener.", 1, "abdominales", 3);
"""

sql_insert_exercises_cardio = """
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Burpees", "Comenzar parado con piernas abiertas a lo ancho de los hombros, agacharse apoyando las manos en el piso, acostarse en el piso, levantarse a posición agachada, pararse dando un salto y aplaudir las manos sobre la cabeza, repetir.", 0, "torso", NULL);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Escalador de montaña", "Apoyarse en el suelo con manos y pies estirando codos y rodillas, llevar una rodilla al pecho mientras el otro pie se mantiene en el piso, alternar y repetir", 0, "torso",  NULL);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Caminar hacia pies", "Apoyarse en el suelo con manos y pies estirando codos y rodillas, caminar con las manos hacia los pies, no es necesario tener los pies estirados al finalizar el movimiento, repetir.", 0, "torso", NULL);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Sentadilla sin/con salto", "Pararse con las piernas abiertas a lo ancho de los hombros, apuntar pies hacia afuera y luego intentar sentarse en el piso, si desea puede dar un salto al estirar las piernas, repetir.", 0, "piernas", NULL);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Estocada sin/con salto", "Pararse comodamente para luego llevar una rodilla al piso flexionando y manteniendo el equilibrio con la pierna contraria, alterar y repetir. Puede alternar las piernas con un salto.", 1, "piernas", NULL);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Escalador de montaña", "Apoyarse en el suelo con manos y pies estirando codos y rodillas, llevar una rodilla al pecho mientras el otro pie se mantiene en el piso, alternar y repetir", 0, "abdominales",  NULL);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Rodillazo al frente", "Pararse comodamente para luego llevar una rodilla de manera explosiva al frente, alternar y repetir.", 0, "abdominales", NULL);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Jumping jacks", "Pararse comodamente para luego simultaneamente abrir piernas y llevar brazos sobre la cabeza, repetir", 0, "cardio",  NULL);
INSERT INTO exercise (name, detail, type, ex_zone, level) values ("Skipping lateral", "Pararse comodamente, dar uno o dos pasos hacia un lado y luego repetir hacia el otro, al dar los pasos llevar rodillas a lo alto de las caderas", 0, "cardio",  NULL);
"""

conn = sqlite3.connect('DBprueba.sqlite')
cur = conn.cursor()
#cur.execute(sql_exercise_table)
#cur.execute(sql_routine_table)
#cur.execute(sql_routine_exercise_table)
cur.execute(sql_insert_exercises_piernas)
cur.execute(sql_insert_exercises_torso)
cur.execute(sql_insert_exercises_abs)
cur.execute(sql_insert_exercises_cardio)
conn.commit()

conn.close()
