from datetime import datetime
import pycron
from pytz import utc
import pendulum
import arrow


def test_dom():
    def run(now):
        assert pycron.is_now('* * * * *', now)
        assert pycron.is_now('* * 18 * *', now)
        assert pycron.is_now('* * */6 * *', now)
        assert pycron.is_now('* * 1,16,18 * *', now)
        assert pycron.is_now('* * 19 * *', now) is False
        assert pycron.is_now('* * */4 * *', now) is False
        assert pycron.is_now('* * 1,16 * *', now) is False
        assert pycron.is_now('* * 1,16 * *', now) is False
        assert pycron.is_now('* * 1-20 * *', now)
        assert pycron.is_now('* * 20-31 * *', now) is False

    now = datetime(2015, 6, 18, 16, 7)
    run(now)
    run(now.replace(tzinfo=utc))
    run(pendulum.instance(now))
    run(arrow.get(now))
