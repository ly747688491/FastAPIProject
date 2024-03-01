from apps.dao.base import BaseDao
from apps.models.user import User


class UserDao(BaseDao):
    def read(self, id: int) -> User:
        return self.db.sess.query(User).filter(
            User.id == id,
            User.is_deleted == 0,
        ).first()

    def read_by_username(self, username: str) -> User:
        return self.db.sess.query(User).filter(
            User.username == username,
            User.is_deleted == 0,
        ).first()
