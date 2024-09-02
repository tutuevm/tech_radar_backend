from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.technologies.schemas import TechnologiesSchema, TechnologiesUpdateSchema
from src.technologies.services import TechnologiesService

tech_router = APIRouter(prefix="/tech", tags=["tech"])


@tech_router.get("/get_all")
async def get_all_technologies(session: AsyncSession = Depends(get_async_session)):
    result = await TechnologiesService().get_all_technologies(session=session)
    return result


@tech_router.post("/create_one")
async def create_new_tech(
    tech: TechnologiesSchema = Depends(),
    session: AsyncSession = Depends(get_async_session),
):
    result = await TechnologiesService().create_point(session=session, tech=tech)
    return result


@tech_router.post("/update_one")
async def update_tech(
    tech: TechnologiesUpdateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    result = await TechnologiesService().update_point(session=session, tech=tech)
    return result
