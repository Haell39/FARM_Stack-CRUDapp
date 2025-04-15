from fastapi import FastAPI
from routes.student import student_router
import uvicorn

# Criando o app com metadados
app = FastAPI(
    title="Student API",
    description="API para gerenciar estudantes usando FastAPI e MongoDB",
    version="1.0.0"
)

# Incluindo routers com prefixo
app.include_router(student_router, prefix="/api")

# Executando o servidor apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
