"""
 DownloadsDao is a generated DAO class. Don't modify it manually.
 http://sqldalmaker.sourceforge.net
"""


from dal.DownloadsInfo import DownloadsInfo


class DownloadsDao:

    def __init__(self, ds):
        self.ds = ds

    def create_download(self, p):
        """
        (C)RUD: downloads
        @type p: DownloadsInfo
        @rtype: int (the number of affected rows)
        """
        sql = """insert into downloads (r_id, d_date, d_downloads) values (?, ?, ?)"""
        return self.ds.exec_dml(sql, [p.r_id, p.d_date, p.d_downloads])

    def update_download(self, p):
        """
        CR(U)D: downloads
        @type p: DownloadsInfo
        @rtype: int (the number of affected rows)
        """
        sql = """update downloads set d_downloads=? where r_id=? and d_date=?"""
        return self.ds.exec_dml(sql, [p.d_downloads, p.r_id, p.d_date])

    def find(self, p_id, p_date):
        """
        @type p_id: str
        @type p_date: str
        @rtype: list[DownloadsInfo]
        """
        sql = """select * from downloads where r_id=? and d_date=?"""
        _res = []

        def _map_cb(row):
            _obj = DownloadsInfo()
            _obj.r_id = row["r_id"]  # t(r_id) <- q(r_id)
            _obj.d_date = row["d_date"]  # t(d_date) <- q(d_date)
            _obj.d_downloads = row["d_downloads"]  # t(d_downloads) <- q(d_downloads)
            _res.append(_obj)

        self.ds.query_all_rows(sql, [p_id, p_date], _map_cb)
        return _res

    def get_latest(self, p_id, start, count):
        """
        @type p_id: int
        @type start: int
        @type count: int
        @rtype: list[DownloadsInfo]
        """
        sql = """select * from downloads 
                where r_id = ? 
                order by d_date DESC 
                limit ?, ?"""
        _res = []

        def _map_cb(row):
            _obj = DownloadsInfo()
            _obj.r_id = row["r_id"]  # t(r_id) <- q(r_id)
            _obj.d_date = row["d_date"]  # t(d_date) <- q(d_date)
            _obj.d_downloads = row["d_downloads"]  # t(d_downloads) <- q(d_downloads)
            _res.append(_obj)

        self.ds.query_all_rows(sql, [p_id, start, count], _map_cb)
        return _res
