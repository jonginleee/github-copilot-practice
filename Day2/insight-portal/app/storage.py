"""인메모리 저장소"""
from typing import Dict, Optional

# 사용자 저장소 (실전에서는 DB 사용)
users_db: Dict[str, Dict] = {}

def get_user_by_email(email: str) -> Optional[Dict]:
    """이메일로 사용자 조회"""
    return users_db.get(email)

def create_user(email: str, hashed_password: str) -> Dict:
    """사용자 생성"""
    user_id = len(users_db) + 1
    user = {
        'id': user_id,
        'email': email,
        'hashed_password': hashed_password
    }
    users_db[email] = user
    return user
