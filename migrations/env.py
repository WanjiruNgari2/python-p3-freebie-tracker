from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context

# Alembic Config
config = context.config

# Logging Setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define the metadata for auto-generation
target_metadata = None  # Change to your models' metadata if available

# Manually define database URL instead of relying on alembic.ini
DATABASE_URL = "postgresql+psycopg2://user:password@localhost/dbname"
config.set_main_option("sqlalchemy.url", DATABASE_URL)

def run_migrations_online():
    """Run migrations in 'online' mode."""
    
    alembic revision --autogenerate -m "Initial migration"
alembic upgrade head


    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )
    with context.begin_transaction():
        context.run_migrations()
else:
    run_migrations_online()
