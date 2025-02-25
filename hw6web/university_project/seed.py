import random
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession
from models import SessionLocal, Group, Student, Teacher, Subject, Grade

fake = Faker()

async def seed_database():
    async with SessionLocal() as session:
        groups = [Group(name=f"Group {i}") for i in range(1, 4)]
        session.add_all(groups)
        await session.commit()

        teachers = [Teacher(name=fake.name()) for _ in range(4)]
        session.add_all(teachers)
        await session.commit()

        subjects = [
            Subject(name=fake.word(), teacher_id=random.randint(1, len(teachers)))
            for _ in range(6)
        ]
        session.add_all(subjects)
        await session.commit()

        students = [
            Student(name=fake.name(), group_id=random.randint(1, len(groups)))
            for _ in range(30)
        ]
        session.add_all(students)
        await session.commit()

        grades = [
            Grade(student_id=random.randint(1, len(students)), subject_id=random.randint(1, len(subjects)),
                  grade=random.randint(50, 100))
            for _ in range(600)
        ]
        session.add_all(grades)
        await session.commit()

import asyncio
asyncio.run(seed_database())
