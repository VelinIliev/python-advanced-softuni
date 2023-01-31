class NameTooShortError(BaseException):
    """Name must be more than 4 characters"""
    pass


class MustContainAtSymbolError(BaseException):
    """ Must Contain At Symbol Error """
    pass


class InvalidDomainError (BaseException):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


class InvalidProviderError (BaseException):
    """You must have a provider"""
    pass


line = input()

while line != 'End':
    data = line.split("@")
    name = data[0]
    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    if len(data) == 1:
        raise MustContainAtSymbolError("Email must contain @")

    domain = data[1].split(".")
    if len(domain) == 1 or len(domain[0]) == 0:
        raise InvalidProviderError("You must have a provider")
    if domain[1] not in ['com', 'bg', 'org', 'net']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')
    line = input()
