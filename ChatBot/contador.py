def actualizar_contador(user_id, contadores):
    if user_id not in contadores:
        contadores[user_id] = 0
    contadores[user_id] += 1
    return contadores[user_id]
