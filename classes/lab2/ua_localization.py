"""
This module defines the UkrainianLocalization class, providing localization strings in Ukrainian.
"""
from .localization import BaseLocalization

class UkrainianLocalization(BaseLocalization):
    """
    UkrainianLocalization class provides localization strings in Ukrainian.
    """
    PROMPT_ENTER_FIRST_NUMBER = "Введіть перше число: "
    PROMPT_ENTER_SECOND_NUMBER = "Введіть друге число: "
    INVALID_INPUT = "Неправильний ввід. Введіть правильне число."
    PROMPT_CHOOSE_OPERATOR = "Виберіть оператор (+, -, *, /, ^, √, %): "
    INVALID_OPERATOR = "Неправильний оператор. Виберіть із списку (+, -, *, /, ^, √, %): "
    PROMPT_ENTER_DECIMAL_PLACES = "Введіть кількість десяткових знаків: "
    RESULT_FORMAT = "Результат: {result:.{decimal_places}f}"
    MEMORY_OPERATOR_HEADER = "Пам'ять оператора:"
    CONTINUE_CALCULATION_PROMPT = "Бажаєте провести ще одне обчислення? (так/ні): "
    CONTINUE_CALCULATION = "так"
    BAN_FOR_ZERO = "Помилка ділення на нуль"
