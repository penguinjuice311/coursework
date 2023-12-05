

class User:
    def get_name(self, email: str):
        table = ["smudge", "kya", "connor", "teddy", "bob", "john", "peter", "jenifer", "person"]
        for name in table:
            if name in email:
                return name
        
        return "connor" 

    def is_walker(self, email: str):
        return "walker" in email

    def email_exists(email: str) -> bool:
        return True 
