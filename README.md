# Alembic

## Extra steps:

1. `$ brew install postgresql`

2. `$ pip install psycopg2`

3. Check with `$ which pg_config`

## Alembic steps

1. On your terminal, run `$ alembic init alembic`

   - it creates a new directory alembic and a new file alembic.ini

2. Go to `alembic.init` and add the database url

   - line 58: `sqlalchemy.url = ADD DATABASE URL HERE`

3. Go to `alembic/env.py` and add your models

```py
from models import Base
target_metadata = Base.metadata
```

4. Create alembic revision

```shell
$ alembic revision --autogenerate -m "First revision"
```
