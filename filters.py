from datetime import datetime

def datetime_filter(timestamp, fmt="%H:%M"):
    return datetime.fromtimestamp(timestamp).strftime(fmt)

app.jinja_env.filters['datetime'] = datetime_filter
