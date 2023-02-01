import re


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


class TooManyAtSymbolsError (BaseException):
    """You have entered too many @"""
    pass


class InvalidSymbolsError (BaseException):
    """You have entered too many @"""
    pass


pattern = r'[.@\w-]+'

line = input()

while line != 'End':
    matches = re.findall(pattern, line)
    if len(matches) > 1:
        raise InvalidSymbolsError("Email must contain only letters, numbers, '@', '_',  '-' or '.'")

    data = line.split("@")
    if len(data) > 2:
        raise TooManyAtSymbolsError('You have entered too many @')
    if len(data) == 1:
        raise MustContainAtSymbolError("Email must contain @")

    name = data[0]
    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    provider, *domain = data[1].split(".")
    if len(provider) == 0:
        raise InvalidProviderError("You must have a provider")
    if domain[-1] not in ['com', 'bg', 'org', 'net']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')
    line = input()
