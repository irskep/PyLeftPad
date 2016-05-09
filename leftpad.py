def leftpad(s, n, ch=' '):
    """
    Adds *n* instances of *ch* on the left side of the string *s*.

    Arguments:
    - *s*: a string
    - *n*: number of instances of *ch* to add on the left
    - *ch*: the character to pad with. Defaults to `' '`.

    Example:

    ```py
    message = "Avoid unnecessary dependencies."
    print(leftpad(s, 2, '!'))
    ```

    Prints:

    ```
    !!Avoid unnecessary dependencies.
    ```
    """
    return ch * n + s