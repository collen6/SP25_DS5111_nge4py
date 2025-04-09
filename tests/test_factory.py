from bin.gainers.factory import GainersFactory
import pytest

def test_factory_yahoo_url():
    factory = GainersFactory("yahoo")
    assert factory.url == "https://finance.yahoo.com/gainers"

def test_factory_wsj_url():
    factory = GainersFactory("wsj")
    assert factory.url == "https://www.wsj.com/market-data/stocks/us/movers"

def test_factory_invalid_source_raises():
    with pytest.raises(ValueError) as exc_info:
        GainersFactory("fake_source")
    assert "Unknown source" in str(exc_info.value)
