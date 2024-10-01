
def add_specialty(specialties_db, name):
    if name in specialties_db:
        return False  # Especialidad ya existe
    specialties_db[name] = {'name': name}
    return True  # Especialidad agregada con éxito
