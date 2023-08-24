def oxford_comma(elements):
    if len(elements) == 0:
        return ""
    elif len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    else:
        oxford_elements = ", ".join(elements[:-1])
        return f"{oxford_elements}, and {elements[-1]}"

result = oxford_comma(["fiddleheads", "okra", "kohlrabi"])
print(result)