from sqlalchemy import func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from models import SessionLocal, Student, Grade, Subject

async def select_1():
    async with SessionLocal() as session:
        result = await session.execute(
            session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
            .join(Grade)
            .group_by(Student.id)
            .order_by(desc('avg_grade'))
            .limit(5)
        )
        return result.all()

async def select_2(subject_id: int):
    async with SessionLocal() as session:
        result = await session.execute(
            session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
            .join(Grade)
            .filter(Grade.subject_id == subject_id)
            .group_by(Student.id)
            .order_by(desc('avg_grade'))
            .limit(1)
        )
        return result.all()
