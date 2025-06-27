from typing import Optional
from constants import Errors,Limits
class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    Methods
    -------
    add(self, numbers)
        Returns the sum of numbers.

    """
    def add(self, numbers: str) -> int:
        """
        Adds numbers provided in a string.

        Parameters
        ----------
        numbers : str
            - An empty string returns 0.
            - A string containing zero or more integers separated by commas (e.g., "1,2,3").
            - A string by delimiters ("\n",",") (e.g., "1\n2,3").
            - A string by custom delimiters between // and \n (e.g., "//;\n1\n2,3").

        Returns
        -------
        int
            The sum of the provided numbers.

        Raises
        ------
        ValueError
            If the input contains:
            - Empty number values (e.g., "1,\n")
            - Negative numbers (e.g., "1,-2,3"), with all negatives listed in the error message
        """
        delemiter=["\n"]
        if not numbers:
            return 0
        
        # check if string start with // if then add to delimeter list
        if numbers.startswith("//"):
            raw_delimiter, numbers = numbers.split("\n", 1)
            if raw_delimiter :
                delemiter.append(raw_delimiter[-1])

        #check for \n replace with , to spling along with , in one go
        for deli in delemiter:
            numbers=numbers.replace(deli, ",")
        parts=numbers.split(",")

        negatives = []
        total = 0
        for part in parts:
            #check invalid inputs
            if part=='':
                raise ValueError(Errors.EMPTY_INPUT)
            #convert number from sting to int
            num = int(part)

            #check negative number
            if num < 0:
                negatives.append(num)

            elif num <= Limits.MAX_NUMBER:
                total += num

        if negatives:
            raise ValueError(Errors.NEGATIVE_NUMBERS.format(negatives))
        
        return total