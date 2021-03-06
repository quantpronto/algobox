import datetime as dt

class ABDataFormat(object):
    pass

class Candle(ABDataFormat):
    def __init__(self, this_dt, topic, open, high, low, close, volume=None):
        self.datetime = this_dt
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.topic = topic

    @property
    def price(self):
        return self.close

    @property
    def average_price(self):
        # exclude volume
        return sum(self.open, self.high, self.low, self.close) / 4

    def __repr__(self):
        return "<algobox.core.format.Candle> {}|{}|O:{}|H:{}|L:{}|C:{}|V:{}".format(
            self.topic, self.datetime.isoformat(), self.open, self.high, self.low,
            self.close, self.volume
        )


    @classmethod
    def from_dict(cls, d):
        volume = d.get("volume", None)
        return cls(
            this_dt=dt.datetime.fromtimestamp(d["datetime"]),
            topic=d["topic"],
            open=d["open"],
            low=d["low"],
            high=d["high"],
            close=d["close"],
            volume=volume,
        )

    def to_dict(self):
        return {
            "datetime": self.datetime.timestamp(),
            "topic": self.topic,
            "open": self.open,
            "low": self.low,
            "high": self.high,
            "close": self.close,
            "volume": self.volume
        }

class Tick(ABDataFormat):
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("the Tick data format is not currently supported")
