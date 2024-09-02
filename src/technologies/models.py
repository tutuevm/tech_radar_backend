from uuid import UUID, uuid4
from sqlalchemy import String
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Technologies(Base):
    __tablename__ = "technologies"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    label: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    x: Mapped[int]
    y: Mapped[int]
    group: Mapped[str] = mapped_column(String(200), nullable=False)
    level: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
