from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_user(name: str, day: int, month: int, year: int):
    """
    Minimal stub for user registration.
    In a full implementation, you would store the user in a database.
    """
    # For now, just return the input as confirmation
    return {
        "message": "User registered (stub)",
        "name": name,
        "dob": f"{day:02d}-{month:02d}-{year:02d}"
    }


@router.get("/list")
def list_users():
    """
    Minimal stub to return a list of users.
    In production, this would query your database.
    """
    return {"users": ["stub user 1", "stub user 2"]}
