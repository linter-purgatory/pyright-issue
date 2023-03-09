# pyright: basic,reportUnknownLambdaType=warning

def fn(unknown_variable_type): # this should be surpressed in basic mode, but isn't
    print(unknown_variable_type)

    lambda y: 1 # this error is correctly turned into a warning via the comment
