from fastapi import APIRouter
from api import auth_router, boards_router, projects_router, spaces_router, tasks_router, users_router, columns_router  # noqa : F401

router = APIRouter()

router.include_router(auth_router)
router.include_router(boards_router)
router.include_router(projects_router)
router.include_router(spaces_router)
router.include_router(tasks_router)
router.include_router(users_router)
router.include_router(columns_router)
