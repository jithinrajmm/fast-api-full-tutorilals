from passlib.context import CryptContext


# for the password hasing 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hashing:
    
    def hashing(password:str):
        return pwd_context.hash(password)
        
    def verify(saved_password:str,user_typed_password:str):
        # first we need to pass the plain password , second is hasded password from the database
        return pwd_context.verify(user_typed_password,saved_password)