
import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value


def test_budget_screen():
    assert repair_quote("screen", "budget", False, False) == 4600


def test_flagship_screen_express():
    assert repair_quote("screen", "flagship", False, True) == 9100


def test_budget_battery_warranty():
    assert repair_quote("battery", "budget", True, False) == 300


def test_flagship_camera():
    assert repair_quote("camera", "flagship", False, False) == 5300


def test_invalid_part():
    with pytest.raises(ValueError):
        repair_quote("speaker", "budget", False, False)


def test_invalid_brand():
    with pytest.raises(ValueError):
        repair_quote("screen", "premium", False, False)


def test_technicians_unavailable():
    assert repair_days("battery", True, 0) == 3


def test_screen_out_of_stock():
    assert repair_days("screen", False, 2) == 6


def test_battery_out_of_stock():
    assert repair_days("battery", False, 2) == 3


def test_trade_in_new_phone():
    assert trade_in_value(10000, 6, False) == 6000


def test_trade_in_medium_age():
    assert trade_in_value(10000, 18, False) == 4000


def test_trade_in_old_phone_cracked():
    assert trade_in_value(10000, 36, True) == 1000


def test_trade_in_too_old():
    assert trade_in_value(10000, 60, False) == 0


def test_invalid_trade_in():
    with pytest.raises(ValueError):
        trade_in_value(-100, 12, False)

def test_screen_warranty():
    assert repair_quote("screen", "budget", True, False) == 4600


def test_camera_out_of_stock():
    assert repair_days("camera", False, 0) == 8


def test_negative_phone_age():
    with pytest.raises(ValueError):
        trade_in_value(10000, -1, False)


def test_zero_original_price():
    with pytest.raises(ValueError):
        trade_in_value(0, 12, False)


def test_trade_in_age_boundaries():
    assert trade_in_value(10000, 12, False) == 6000
    assert trade_in_value(10000, 24, False) == 4000
    assert trade_in_value(10000, 48, False) == 2000
    assert trade_in_value(10000, 49, False) == 0


def test_charging_port_express():
    assert repair_quote("charging_port", "budget", False, True) == 1600
