class NameTooShortError(BaseException):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(BaseException):
    """ Must Contain At Symbol Error """
    pass


class InvalidDomainError (BaseException):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


while True:
    data = input()
    if data == 'End':
        break
    data = data.split("@")
    name = data[0]
    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    if len(data) == 1:
        raise MustContainAtSymbolError("Email must contain @")
    domain = data[1].split(".")[1]
    if domain not in ['com', 'bg', 'org', 'net']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print('Email is valid')
