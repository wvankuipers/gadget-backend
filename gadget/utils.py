from datetime import datetime, timezone


def serialize_list(list_items, recursive=True):
    """Serialize a list of items, mostly to serialize database models"""
    return [i.serialize(recursive) for i in list_items]


def to_local_js_timestamp(utc_datetime):
    """Convert a UTC datetime into a local time timestamp suitable for the JavaScript date object"""
    return int(datetime.timestamp(utc_datetime.replace(tzinfo=timezone.utc).astimezone(tz=None)) * 1000)
