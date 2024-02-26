# Alembic for db migrations
- alembic revision --autogenerate -m "Add is_admin to Users"
- check the changes in alembic/version/revision_id_name.py
- alembic upgrade head