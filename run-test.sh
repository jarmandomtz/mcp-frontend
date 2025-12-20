source venv3.11/bin/activate

pip install ipympl ipython jupyterlab matplotlib nodejs numpy seaborn starlette fastapi pytest itsdangerous pydantic_settings passlib google-cloud-bigquery python-multipart

pip install -e .

pytest -q