from typing import Optional
class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    Methods
    -------
    add(a, b)
        Returns the sum of a and b.

    """
    def add(self, numbers: str) -> int:
        """
        Adds numbers provided in a  string.

        Parameters
        ----------
        numbers : str
            A string containing zero or more integers separated by commas (e.g., "1").
            An empty string returns 0.

        Returns
        -------
        int
            The sum of the provided numbers.
        """
        
        if not numbers:
            return 0
        delemiter=["\n"]
        #check for \n replace with , to spling along with , in one go
        for deli in delemiter:
            numbers=numbers.replace(deli, ",")
        parts=numbers.split(",")
        if '' in parts:
            raise ValueError("Invalid input")


        total = sum(int(part) for part in parts)
        return int(total)