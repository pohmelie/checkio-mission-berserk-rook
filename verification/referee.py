from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS


cover = """def cover(func, data):
    return func(data[0], set(data[1]))
"""


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover,  # or None
            'python-3': cover
        },
        function_name="berserk_rook"
        # checker=None,  # checkers.float.comparison(2)
        # add_allowed_modules=[],
        # add_close_builtins=[],
        # remove_allowed_modules=[]
    ).on_ready)
