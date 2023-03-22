from collections.abc import Callable
from typing import List, TypeVar

T = TypeVar("T")


def parse_input(
    input_message: str,
    *,
    input_validation: Callable[[T], bool] = None,
    valid_input: List[T] = None,
    pre_process_input: Callable[[str], T] = None,
    error_message: str = None,
) -> T:
    if input_validation and callable(input_validation):
        return parse_input_from_validation_function(
            input_message=input_message,
            input_validation=input_validation,
            error_message=error_message,
            pre_process_input=pre_process_input,
        )
    if valid_input:
        input_validation = lambda x: x in valid_input
        return parse_input_from_validation_function(
            input_message=input_message,
            input_validation=input_validation,
            error_message=error_message,
            pre_process_input=pre_process_input,
        )
    raise Exception(
        "Can't validate input. Inform input_validation function OR list of valid_input"
    )


def parse_input_from_validation_function(
    input_message: str,
    input_validation: Callable[[T], bool],
    pre_process_input: Callable[[str], T] = None,
    error_message: str = None,
) -> T:
    if pre_process_input is None or not callable(pre_process_input):
        pre_process_input = lambda x: x

    initial_input = pre_process_input(input(input_message))
    while not input_validation(initial_input):
        if error_message:
            print(error_message)
        initial_input = pre_process_input(input(input_message))
    return initial_input
