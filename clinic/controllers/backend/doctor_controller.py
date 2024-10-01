
def add_doctor(doctors_db, name, specialty, schedule):
    if name in doctors_db:
        return False  # Médico ya existe
    doctors_db[name] = {'name': name, 'specialty': specialty, 'schedule': schedule}
    return True  # Médico agregado con éxito
