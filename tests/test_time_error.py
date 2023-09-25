from unittest.mock import Mock
import time
from lib.time_error import TimeError

def test_if_error_returns_time():
    requester_mock = Mock()
    response_mock = Mock()
    the_time = Mock()

    the_time.time.return_value = 1695655504

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {"abbreviation":"BST","client_ip":"31.94.66.100","datetime":"2023-09-25T16:26:44.241504+01:00","day_of_week":1,"day_of_year":268,"dst":True,"dst_from":"2023-03-26T01:00:00+00:00","dst_offset":3600,"dst_until":"2023-10-29T01:00:00+00:00","raw_offset":0,"timezone":"Europe/London","unixtime":1695655604,"utc_datetime":"2023-09-25T15:26:44.241504+00:00","utc_offset":"+01:00","week_number":39}

    timer = TimeError(requester_mock, the_time)
    result = timer.error()
    assert result == 1695655604 - the_time.time()