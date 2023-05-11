<h1>PatternCalculator</h1>

<p>The <code>PatternCalculator</code> class is a calculator that evaluates a mathematical expression using the given dictionary of variables and values. The class is initialized with two parameters, <code>dict</code> and <code>pattern</code>.</p>
<p><code>dict</code> is a Python dictionary where the keys represent variable names and the values represent their corresponding values.</p>
<p><code>pattern</code> is a string that contains the name of the expression and the expression itself, separated by a pipe (<code>|</code>). The expression can contain variables that are defined in the <code>dict</code>, as well as the standard mathematical operators <code>+</code>, <code>-</code>, <code>*</code>, and <code>/</code>.</p>
<p>The class has three instance variables:</p>
<ul>
<li><code>dict</code>: stores the dictionary of variables and values</li>
<li><code>pattern</code>: stores the pattern string</li>
<li><code>values_stack</code>: stores a stack of operand values during the evaluation of the expression</li>
<li><code>op_stack</code>: stores a stack of operators during the evaluation of the expression</li>
</ul>
<p>The class has two methods:</p>
<ul>
<li><code>apply_operator()</code>: pops the top two values from <code>values_stack</code>, pops the top operator from <code>op_stack</code>, applies the operator to the two values, and pushes the result onto <code>values_stack</code>.</li>
<li><code>evaluate()</code>: evaluates the expression in <code>pattern</code> and returns a tuple containing the name of the expression and its evaluated value.</li>
</ul>
<p>The <code>evaluate()</code> method first splits <code>pattern</code> into the name and the expression, and then replaces all the variables in the expression with their corresponding values from <code>dict</code>. It then parses the resulting expression and evaluates it using the operator stacks and operand stacks. It checks for invalid expressions or invalid use of parentheses, and raises a <code>ValueError</code> if it encounters any. Finally, it returns a tuple containing the name of the expression and its evaluated value.</p>
<p>Example usage:</p>


```python
variables = {'a': 1, 'b': 2}
pattern = 'expr | (a + b) * 2'
calculator = PatternCalculator(variables, pattern)
name, result = calculator.evaluate()
print(f"{name}: {result}") # expr: 6.0
```

