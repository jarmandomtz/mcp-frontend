# Create users

Steps,
- Using hash_password.py create a password hash
- Insert a user record in BQ users table 
    - Using console with the example file users.sql
    - Using CLI (example command bellow)
- Review user was inserted (example list-users.sql)

<details close>
<summary>Generate password hash</summary>

```shell
source ../venv3.11/bin/activate

which pip
pip install "passlib[argon2]"

python3 hash_password.py
Enter password to hash: Jorgearmand.

Argon2 hash:
$argon2id$v=19$m=65536,t=3,p=4$tFZqrTXmPKe0ljLGmFPqvQ$hEc0S3i5wINxMgDqG21y5fVhJ93s4XTGqsG908X4Le4
```

</details>

<details close>
<summary>Insert user using CLI</summary>

```shell
bq query --use_legacy_sql=false \
'INSERT INTO `PROJECT_ID.mcp_sre_assistant.users`
(email, password_hash, role, created_at)
VALUES (
  "user@example.com",
  "$argon2id$v=19$m=65536,t=3,p=2$...",
  "user",
  CURRENT_TIMESTAMP()
)'
```

</details>

<details close>
<summary>Generate user with python script create_user.py</summary>

```shell
source ../venv3.11/bin/activate

which pip
pip install "passlib[argon2]"

python3 create_user.py

Email: jarmando_ml@hotmail.com
Password: jorgearmando
Role (admin/user/viewer): user
✅ User created successfully
```

</details>