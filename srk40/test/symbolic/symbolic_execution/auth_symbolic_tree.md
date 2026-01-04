Symbolic Execution Tree (AuthService.login)

Inputs:
- u: username (symbolic)
- p: password (symbolic)

Node 1: user_exists(u)?
  Path A: False -> return failure ("unknown user")
  Path B: True  -> Node 2

Node 2: password_matches(u, p)?
  Path B1: False -> return failure ("wrong password")
  Path B2: True  -> return success (authenticated)
