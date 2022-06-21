from opylib import db_cache

from bot.common.cog_common import CogCommon
from conf import Conf

conf = Conf.Settings
"""Map class with setting for this cog to variable"""


class CogSettings(CogCommon, name='Settings'):
    def __init__(self, db: db_cache):
        super().__init__(db, conf=conf)
