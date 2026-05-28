import pytest
import utils


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)]
)
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected ", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (4, "100"),
        (5, "101"),
        (10, "1010"),
        (100, "1100100"),
    ],
)
def test_decimal_to_binary_returns_correct_binary_value(a, expected):
    assert utils.decimal_to_binary(a) == expected


@pytest.mark.parametrize("a", [-1, 101, 150])
def test_decimal_to_binary_raises_value_error_for_number_outside_range(a):
    with pytest.raises(ValueError):
        utils.decimal_to_binary(a)


@pytest.mark.parametrize("a", ["10", 2.5, None, True])
def test_decimal_to_binary_raises_type_error_for_invalid_type(a):
    with pytest.raises(TypeError):
        utils.decimal_to_binary(a)
