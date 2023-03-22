import unittest
from unittest.mock import patch

import pytest

from core.input import parse_input, parse_input_from_validation_function


def test_parse_input_from_validation_function(mocker):
    mock_input = mocker.patch("builtins.input", return_value="1")
    input_validation = lambda x: x == 1
    pre_process_input = int
    input_message = "input message"
    input_provided = parse_input_from_validation_function(
        input_message,
        input_validation=input_validation,
        pre_process_input=pre_process_input,
    )
    assert input_provided == 1
    mock_input.assert_called_with(input_message)


def test_parse_input(mocker):
    mock_input = mocker.patch("builtins.input", return_value="1")
    input_validation = lambda x: x == 1
    pre_process_input = int
    input_message = "input message"
    input_provided = parse_input(
        input_message,
        input_validation=input_validation,
        pre_process_input=pre_process_input,
    )
    assert input_provided == 1
    mock_input.assert_called_with(input_message)


def test_parse_input_when_no_validation_or_valid_input_defined(mocker):
    with pytest.raises(Exception, match="Can't validate input"):
        mocker.patch("builtins.input", return_value="test")
        parse_input("Enter a value: ")


def test_parse_input_when_only_validation_function_defined(mocker):
    validation_function = lambda x: x.isdigit()
    mocker.patch("builtins.input", side_effect=["hello", "world", "123"])
    assert (
        parse_input("Enter a number: ", input_validation=validation_function) == "123"
    )


def test_parse_input_when_only_valid_input_defined(mocker):
    valid_input = ["yes", "no"]
    mocker.patch("builtins.input", side_effect=["y", "no"])
    assert parse_input("Enter yes or no: ", valid_input=valid_input) == "no"


def test_parse_input_from_validation_function_when_input_is_invalid(mocker):
    validation_function = lambda x: x.isdigit()
    error_message = "Invalid input. Enter a number: "
    mocker.patch("builtins.input", side_effect=["hello", "world", "123"])
    assert (
        parse_input_from_validation_function(
            "Enter a number: ", validation_function, error_message=error_message
        )
        == "123"
    )


def test_parse_input_from_validation_function_when_pre_processing_is_defined(mocker):
    pre_process_input = lambda x: x.strip().lower()
    mocker.patch("builtins.input", return_value="YES")
    assert (
        parse_input_from_validation_function(
            "Enter yes or no: ",
            lambda x: x == "yes",
            pre_process_input=pre_process_input,
        )
        == "yes"
    )


class TestInput(unittest.TestCase):
    def test_parse_input_from_validation_function_with_pre_process_input(self):
        def pre_process_input(input_str):
            return input_str.strip().lower()

        input_validation = lambda x: x == "yes"

        with patch("builtins.input", return_value=" YES ") as mocked_input:
            result = parse_input_from_validation_function(
                input_message="Type 'yes' to continue: ",
                input_validation=input_validation,
                pre_process_input=pre_process_input,
            )

        self.assertEqual(result, "yes")
        mocked_input.assert_called_once_with("Type 'yes' to continue: ")

    def test_parse_input_from_validation_function_without_pre_process_input(self):
        input_validation = lambda x: x.isdigit() and int(x) < 10

        with patch("builtins.input", side_effect=["11", "12", "5"]) as mocked_input:
            result = parse_input_from_validation_function(
                input_message="Enter a number less than 10: ",
                input_validation=input_validation,
                error_message="Invalid input! Try again.",
            )

        self.assertEqual(result, "5")
        self.assertEqual(mocked_input.call_count, 3)
