if func.__name__ == "add":
    if len(param_list) > 0:
        name = param_list[0]
        phone = param_list[1]
        match = re.fullmatch(r'\+\d{12}', phone)
        if match:
            result = func(param_list)
        else:
            result = f"""Entered value \"{phone}\" is not correct.\nPhone must start with \"+\" and must have 12 digits.\nFor example: \"+380681235566\"\n\nTRY AGAIN!!!"""
    else:
        result = f"""Command \"{func.__name__}\" reqired 1 or 2 arguments: name and phone.\nFor example: {func.__name__} [name] - To add a new contact without phones\nFor example: {func.__name__} [name] [phone] - To add a new contact with phones, or add new phone to contact\n\nTRY AGAIN!!!"""
