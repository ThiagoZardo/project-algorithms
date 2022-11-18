def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None
    
    connected_students = 0
    for login, logout in permanence_period: # Aqui atribuo login e logout para os indices 0 e 1.
        if not isinstance(login, int) or not isinstance(logout, int):
            return None
        if login <= target_time <= logout:
            connected_students += 1
    return connected_students
