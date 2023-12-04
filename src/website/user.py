

class User:
    def get_name(self, email: str):
        if email == "kya@gmail.com":
            return "kya"
        return "connor" 

    def is_walker(self, email: str):
        return "walker" in email

    def email_exists(email: str) -> bool:
        return True 
