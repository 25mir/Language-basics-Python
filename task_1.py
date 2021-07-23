import re


def email_parse(email_address):
    pattern = re.compile(r'(?P<username>\w+).(?P<domain>\w+\.\w+)')
    result_iter = pattern.finditer(email_address)
    for result in result_iter:
        print(result.groupdict())


email_parse('someone@geekbrains.ru')
