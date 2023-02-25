from flask import Flask
from yoyo import read_migrations, get_backend
import os
app = Flask(__name__)

app.config['DB_USERNAME'] = 'postgres'
app.config['DB_PASSWORD'] = 'admin'
app.config['DB_HOST'] = 'localhost'
app.config['DB_PORT'] = 5432
app.config['DB_NAME'] = 'test'

backend = get_backend(f"postgresql://{app.config['DB_USERNAME']}:{app.config['DB_PASSWORD']}@{app.config['DB_HOST']}:{app.config['DB_PORT']}/{app.config['DB_NAME']}")

migrations_folder = "migrations"
migrations = read_migrations(migrations_folder)
print(f'migrations: {migrations}')
if migrations:
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
        print("Migraciones aplicadas correctamente.")

if __name__ == "__main__":
    app.run()