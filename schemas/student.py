# Função para converter um documento MongoDB em um dicionário JSON
def studentEntity(db_item) -> dict:
    return {
        'id': str(db_item['_id']),  # Convertendo ObjectId para string
        'name': db_item['student_name'],
        'email': db_item['student_email'],
        'phone': db_item['student_phone']
    }

# Converte uma lista de documentos MongoDB em uma lista de dicionários JSON
def listOfStudentEntity(db_item_list) -> list:
    return [studentEntity(item) for item in db_item_list]  # Usando list comprehension (ainda estudando)
