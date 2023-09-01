string = "Aa Bb Cc"
if "aa" in string.lower():
    string = string.lower().replace("aa", "")
print(string)