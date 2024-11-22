def all_variants(text):
    for dif in range(1, len(text) + 1):
        for sli in range(len(text)):
            yield text[sli:sli + dif]
            if sli + dif == len(text):
                break

a = all_variants("abc")
for i in a:
    print(i)
