INSERT INTO `PROJECT_ID.mcp_sre_assistant.users` (email, password_hash, role, created_at)
VALUES (
  'admin@example.com',
  '$argon2id$v=19$m=65536,t=3,p=2$...hash...',
  'admin',
  CURRENT_TIMESTAMP()
);
