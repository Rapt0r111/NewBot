from modules import * 
from . import main, inline, states

router = Router()

router.include_router(main.router)
router.include_router(inline.router)
router.include_router(states.router)