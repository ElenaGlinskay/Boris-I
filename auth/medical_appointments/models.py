from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    role = db.StringField(required=True)  # Super Admin, Admin, Medico, Paciente

class Medico(User):
    nombre = db.StringField(required=True)
    especialidades = db.ListField(db.StringField())

class Paciente(User):
    nombre = db.StringField(required=True)
    telefono = db.StringField()
    citas = db.ListField(db.ReferenceField('Cita'))

class Especialidad(db.Document):
    nombre = db.StringField(required=True)
    descripcion = db.StringField()

class Cita(db.Document):
    paciente_id = db.ReferenceField(Paciente)
    medico_id = db.ReferenceField(Medico)
    especialidad_id = db.ReferenceField(Especialidad)
    fecha = db.DateTimeField()
    estado = db.StringField(choices=["Pendiente", "Confirmada", "Cancelada"])
