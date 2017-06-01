import tarsier
import datetime

import pytz
import rethinkdb as r



class TarsierInputRethinkdb(tarsier.TarsierInputPlugin):
    def init_plugin(self, table, time_condition, host="127.0.0.1", port=28015, db="test", user="admin", password="", timeout=20, ssl=[]):
        self._conn = r.connect(host=host, port=int(port), db=db, user=user, password=password, timeout=timeout, ssl=ssl)
        self._time_condition = time_condition
        self._table = table

    def load(self):
        lt = datetime.datetime.now(tz=pytz.utc)
        gte = lt - datetime.timedelta(**self._time_condition["duration"])

        ret = r.table(self._table)\
            .filter(
                (r.row[self._time_condition["field"]] >= gte) & (r.row[self._time_condition["field"]] < lt)
            ).run(self._conn)
        return list(ret)

