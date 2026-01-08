from fastapi import FastAPI
from app import models, database
from app.routers import voting_router

app = FastAPI(title="Sistem Voting Online")

# Buat tabel otomatis saat aplikasi jalan
models.Base.metadata.create_all(bind=database.engine)

# Ambil rute dari router
app.include_router(voting_router.router)

@app.get("/")
def home():
    return {"status": "Backend Voting Aktif"}