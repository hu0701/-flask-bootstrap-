from datetime import datetime
from routes import db
from sqlalchemy import Integer, String, BLOB, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column


class Article(db.Model):
    """
    踩坑，
    1、nullable参数写错
    2、格式不对齐
    """
    __tablename__ = 'articles'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    __content: Mapped[bytes] = mapped_column(BLOB, name="content", nullable=False)
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    update_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    @property
    def content(self):
        return self.__content.decode('utf-8')
