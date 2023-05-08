from modules import * 
from . import main, inline, states, help, catalog

router = Router()

router.include_router(main.router)
router.include_router(help.router)
router.include_router(inline.router)
router.include_router(states.router)
router.include_router(catalog.router)
