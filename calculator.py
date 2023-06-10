import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


class PatternCalculator:
    """
    A class for evaluating mathematical expressions using a pattern and a
    dictionary of variables.

    Attributes:

    dict (dict): a dictionary containing variable names and values.

    pattern (str): a string representing the pattern of the expression.

    values_stack (list): a list to store the operands of the expression.

    op_stack (list): a list to store the operators of the expression.

    Methods:

    apply_operator(): pops the two top operands from the values_stack and the
    top operator from op_stack, applies the operator to the operands, and
    pushes the result back to the values_stack.

    evaluate(): evaluates the expression and returns a tuple containing the
    name of the expression and its value.
    """

    def __init__(self, dict, pattern):
        self.dict = dict
        self.pattern = pattern
        self.values_stack = []
        self.op_stack = []

    def apply_operator(self):
        right = self.values_stack.pop()
        left = self.values_stack.pop()
        operation = OPERATORS.get(self.op_stack.pop())
        self.values_stack.append(operation(left, right))

    def evaluate(self):
        name, formula = self.pattern.split(' | ')
        instance = ''
        for item in formula.split(' '):
            instance += (
                str(self.dict.get(item)) if self.dict.get(item) else item
            )
        exp = instance.replace(',', '.')
        i = 0
        parentheses = 0
        while i < len(exp):
            ch = exp[i]
            if ch.isdigit():
                start = i
                while i < len(exp) and (exp[i].isdigit() or exp[i] == '.'):
                    i += 1
                num = float(exp[start:i])
                self.values_stack.append(num)
                continue
            if ch in ('+', '-'):
                while self.op_stack and self.op_stack[-1] in ('*', '/'):
                    self.apply_operator()
                self.op_stack.append(ch)
            elif ch in ('*', '/'):
                while self.op_stack and self.op_stack[-1] in ('*', '/'):
                    self.apply_operator()
                self.op_stack.append(ch)
            elif ch == '(':
                self.op_stack.append(ch)
                parentheses += 1
            elif ch == ')':
                if parentheses == 0:
                    raise ValueError('Invalid parentheses in expression')
                while self.op_stack[-1] != '(':
                    self.apply_operator()
                self.op_stack.pop()
                parentheses -= 1
            else:
                raise ValueError(f'Invalid character in expression: {ch}')
            i += 1

        if parentheses != 0:
            raise ValueError('Invalid parentheses in expression')

        while self.op_stack:
            self.apply_operator()

        return name, self.values_stack[-1]


if __name__ == '__main__':
    pattern = 'объём | длина *  ширина * высота'
    dict = {
        'длина': '10,5',
        'ширина': 15.5,
        'высота': 5,
    }
    print(PatternCalculator(dict, pattern).evaluate())
