def check_palindrom(kata):
    if kata == kata [::-1]:
        return f"{kata} adalah palindrom"
    else:
        return f"{kata} bukan palindrom"

kata = "level"      
print(check_palindrom(kata))
    