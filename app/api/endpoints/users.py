'''
All endpoints related to user data
'''
from fastapi import APIRouter
from app.models.users import UserCreate, UserLogin
from app.repositories.user import create_user, login_user
from app.utils.security import hash_password, verify_password

router = APIRouter()

@router.post("/register_user")
async def create_user_handler(user_data: UserCreate):
    
    # Hash the password
    hashed_password = hash_password(user_data.password)

    # Replace the plaintext password with the hashed password
    user_data.password = hashed_password
    
    # Create the user
    user_id = create_user(user_data)
    
    if isinstance(user_id, str):
        return {"message": "User created successfully", "user_id": user_id}
    else:
        return user_id
    
    
@router.post("/login_user")
async def login_user_handler(user_data: UserLogin):
    
    # Check that the email exists, if so, retrieve pass
    password = login_user(user_data)
    
    #Check if theres a pass or the email didnt matched with any record
    if isinstance(password, str):
        # If account exists, check the password
        if (verify_password(user_data.password,password)):
             return {"message": "Login successful", "login":"true"}
        else:
            return {"message": "Invalid email or password!"}
                   
    else:
        # Print no email match error
        return password