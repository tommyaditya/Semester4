class Authentication:
    def login(self):
        raise NotImplementedError("Subclasses must implement this method")

class EmailPasswordAuth(Authentication):
    def login(self, email, password):
        return f"User {email} logged in using email and password."

class GoogleAuth(Authentication):
    def login(self, google_token):
        return "User logged in using Google authentication."

class FingerprintAuth(Authentication):
    def login(self, fingerprint_data):
        return "User logged in using fingerprint authentication."

auth_methods = [
    EmailPasswordAuth(),
    GoogleAuth(),
    FingerprintAuth()
]

print(auth_methods[0].login("user@example.com", "securepassword"))
print(auth_methods[1].login("google_token_123"))
print(auth_methods[2].login("fingerprint_data"))
