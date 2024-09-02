from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Technologies
from .schemas import TechnologiesSchema, TechnologiesUpdateSchema

from math import pi, cos, sin

from src.settings import settings


class CoordinateCalculator:
    def __init__(self):
        self.radius_settings = settings.RADAR_SETTINGS

    def calculate_initial_coordinates(self, tech_data):
        radius = self.radius_settings.LEVEL_RANGES[tech_data["level"]][
            tech_data["using_num"] - 1
        ]
        start_angle, end_angle = self.radius_settings.QUARTER_RANGES[tech_data["group"]]
        angle = start_angle + pi / 180 * 5
        x = radius * cos(angle) + self.radius_settings.RADIUS
        y = radius * sin(angle) + self.radius_settings.RADIUS
        return x, y, radius, angle

    def find_free_spot(self, radius, existing_points, angle):
        new_x, new_y = self._calculate_coordinates(radius, angle)
        new_angle = angle
        while self._is_point_occupied(new_x, new_y, existing_points):
            new_angle += pi / 180 * 3
            if new_angle - angle >= pi / 180 * 80:
                new_angle = angle
                radius += 10
            new_x, new_y = self._calculate_coordinates(radius, new_angle)

        return new_x, new_y

    def _calculate_coordinates(self, radius, angle):
        x = radius * cos(angle) + self.radius_settings.RADIUS
        y = radius * sin(angle) + self.radius_settings.RADIUS
        return x, y

    def _is_point_occupied(self, x, y, existing_points):
        for point in existing_points:
            if (
                point[0] - 20 <= x <= point[0] + 20
                and point[1] - 20 <= y <= point[1] + 20
            ):
                return True
        return False


class TechnologiesService:
    def __init__(self):
        self.coordinate_calculator = CoordinateCalculator()

    async def update_point(self, session: AsyncSession, tech: TechnologiesUpdateSchema):
        """updating an existing point"""
        tech_data = tech.data.model_dump()
        stmt = (
            update(Technologies).where(Technologies.id == tech.id).values(**tech_data)
        )
        await session.execute(stmt)
        await session.commit()

    async def get_all_technologies(self, session: AsyncSession):
        query = select(Technologies)
        result = await session.execute(query)
        result = [row[0] for row in result.all()]
        return result

    async def create_point(self, session: AsyncSession, tech: TechnologiesSchema):
        """Calculate coordinates and create a point"""
        tech_data = tech.model_dump()
        x, y, radius, angle = self.coordinate_calculator.calculate_initial_coordinates(
            tech_data
        )
        quarter_and_level_points = await session.execute(select(Technologies))
        existing_points = [
            (row[0].x, row[0].y) for row in quarter_and_level_points.all()
        ]
        if existing_points:
            x, y = self.coordinate_calculator.find_free_spot(
                radius, existing_points, angle
            )

        data = {
            "label": tech_data["label"],
            "group": tech_data["group"].value,
            "level": tech_data["level"].value,
            "description": tech_data["description"],
            "x": x,
            "y": y,
        }

        stmt = insert(Technologies).values(**data)
        await session.execute(stmt)
        await session.commit()
