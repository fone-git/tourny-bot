from utils.dict_persistent import DictPersistent
from utils.log import log


def get_db() -> dict:
    """
    Access to REPL DB
    :return:
    """
    try:
        # noinspection PyUnresolvedReferences
        from replit import db
        log("Imported access to REPL DB")
    except ModuleNotFoundError:
        db = DictPersistent()
        log("Unable to get REPL DB Using Local dict")
    return db
