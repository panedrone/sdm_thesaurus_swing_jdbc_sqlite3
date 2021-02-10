"""
 ReleasesDao is a generated DAO class. Don't modify it manually.
 http://sqldalmaker.sourceforge.net
"""


from dal.Release import Release


class ReleasesDao:

    def __init__(self, ds):
        self.ds = ds

    def create_release(self, p):
        """
        (C)RUD: releases
        Generated values are passed to DTO.
        @type p: Release
        @rtype: None
        @raise: Exception if no rows inserted.
        """
        sql = """insert into releases (r_name) values (?)"""
        _ai_values = [["r_id", None]]
        self.ds.insert_row(sql, [p.r_name], _ai_values)
        p.r_id = _ai_values[0][1]

    def find_by_name(self, r_name):
        """
        @type r_name: str
        @rtype: list[Release]
        """
        sql = """select * from releases where r_name = ?"""
        _res = []

        def _map_cb(row):
            _obj = Release()
            _obj.r_id = row["r_id"]  # t(r_id) <- q(r_id)
            _obj.r_name = row["r_name"]  # t(r_name) <- q(r_name)
            _res.append(_obj)

        self.ds.query_all_rows(sql, [r_name], _map_cb)
        return _res
