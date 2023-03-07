# 0x01-python-if_else_loops_functions

Contains Python scripts that make use of loops, functions and conditionals.

Also has a C source file.

## Python Scripts

### 0-positive_or_negative.py

Assigns a random signed number to variable `number` each time it's executed and prints whether the number is positive or negative.

### 1-last_digit.py

Assigns a random number to variable `number` each time it's executed and prints the last digit of the number.

### 2-print_alphabet.py

Prints the ASCII alphabet, in lowercase, not followed by a new line.

### 3-print_alphabt.py

Prints the ASCII alphabet except the letters `e` and `q`, in lowercase, not followed by a new line.

### 4-print_hexa.py

Prints all numbers from `0` to `98` in decimal and in hexadecimal.

``` Python
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
...
96 = 0x60
97 = 0x61
98 = 0x62
```

### 5-print_comb2.py

Prints numbers from `0` to `99`.

- Numbers are separated by `,`, followed by a space.
- Numbers are printed in ascending order, with two digits.
- The last number is followed by a new line.

### 6-print_comb3.py

Prints all possible different combinations of two digits.

- Numbers are separated by `,`, followed by a space.
- The two digits must be different.
- `01` and `10` are considered the same combination of the two digits 0 and 1.
- Prints only the smallest combination of two digits.
- Numbers sare printed in ascending order, with two digits.
- The last number is followed by a new line.

### 7-islower.py

Contains a function that checks for lowercase character.

Prototype:

``` Python
def islower(c):
```

-Returns `True` if `c` is lowercase
-Returns `False` otherwise

### 8-uppercase.py

Contains a function that prints a string in uppercase followed by a new line.

Prototype:

``` Python
def uppercase(str):
```

### 9-print_last_digit.py

Contains a function that prints the last digit of a number.

Prototype:

```Python
def print_last_digit(number):
```

Returns the value of the last digit

### 10-add.py

Contains a function that adds two integers and returns the result.

Prototype:

```Python
def add(a, b):
```

### 11-pow.py

Contains a function that computes `a` to the power of `b` and returns the value.

Prototype:

```Python
def pow(a, b):
```

### 12-fizzbuzz.py

Contains a function that prints the numbers from 1 to 100 separated by a space.

- For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
- For numbers which are multiples of both three and five print FizzBuzz.

Prototype:

```Python
def fizzbuzz():
```

### 100-print_tebahpla.py

Prints the ASCII alphabet in reverse order, alternating lowercase and uppercase(`z` in lowercase and `Y` in uppercase), not followed by a new line.

### 101-remove_char_at.py

Contains a function that creates a copy of the string, removing the character at the position `n`(not the Python way, the "C array index").

Prototype:

```Python
def remove_char_at(str, n):
```

### 102-magic_calculation.py

Contains a Python function

```Python
def magic_calculation(a, b, c):
```

that does exactly same as the following Python bytecode:

```text
 3           0 LOAD_FAST                 0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```

## C Source Code

### 13-insert_number.c

Contains a function that inserts a number into a sorted singly linked list.

Prototype:

```C
listint_t *insert_node(listint_t **head, int number);
```

### lists.h

Contains function prototypes used in manipulatin of linked lists of type `listint_t` and type description for the `listint_t` struct.
