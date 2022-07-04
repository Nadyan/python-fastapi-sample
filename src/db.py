"""
    Fake db for testing
"""

from typing import List
from uuid import UUID

from models import User, Gender, Role

db: List[User] = [
    User(
        id=UUID("d42310fd-7a4f-4d09-ad46-a3821330af2e"), 
        first_name = "Nadyan", 
        last_name = "Pscheidt",
        middle_name = "Suriel",
        gender = Gender.male,
        roles = [Role.student]
    ),
    User(
        id=UUID("3fe0a2dd-1e95-4a12-b8d0-a37fc154f24b"), 
        first_name = "Larissa", 
        last_name = "Pscheidt",
        middle_name = "Stoeberl",
        gender = Gender.female,
        roles = [Role.student, Role.user]
    )
]
