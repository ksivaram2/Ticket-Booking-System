Concolic Constraints for AuthService.login

Path 1 (unknown user):
- user_exists(u) = False
Example: u="no_such_user", p="AnyPass123"

Path 2 (wrong password):
- user_exists(u) = True
- password_matches(u, p) = False
Example: u="sym_user2", p="bad"

Path 3 (success):
- user_exists(u) = True
- password_matches(u, p) = True
Example: u="c_user", p="Cpass12345"
