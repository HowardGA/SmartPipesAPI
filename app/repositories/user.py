from app.utils.database import db
from app.models.users import UserCreate, UserLogin

def create_user(user_data: UserCreate):
    # Check if email is already registered
    existing_user = db.Users.find_one({"email": user_data.email})
    
    if existing_user:
        return {"message": "Email already registered"}
    
    # Logic to insert user data into the database
    result = db.Users.insert_one(dict(user_data))
    return str(result.inserted_id)


def login_user(user_data: UserLogin):
    # Check if email exists
    existing_user = db.Users.find_one({"email": user_data.email})
    
    if existing_user:
        # If theres an existan user, get his pass
        user_pass = existing_user.get("password")
        return str(user_pass)
    
    else:
        return {"message": "Invalid email or password!", "login": "false"}
