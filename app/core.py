from datetime import timedelta, datetime
from typing import Union
from jose import JWTError, jwt
from passlib.context import CryptContext
import os

# Load secret key (CHANGE IN PROD)
SECRET_KEY = os.getenv("SECRET_KEY", "change_this_secret_for_prod")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days

# -------------------------------------------------------
# PASSWORD HASHING (ARGON2)
# -------------------------------------------------------
pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

def get_password_hash(password: str) -> str:
    """Hash password using Argon2 (no length limit, secure)."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password using Argon2."""
    return pwd_context.verify(plain_password, hashed_password)


# -------------------------------------------------------
# JWT TOKEN CREATION
# -------------------------------------------------------
def create_access_token(
    data: dict,
    expires_delta: Union[timedelta, None] = None
):
    """Create JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
