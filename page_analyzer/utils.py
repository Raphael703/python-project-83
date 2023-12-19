from urllib.parse import urlparse, urlunparse

from validators.url import url as url_validator


def normalize_url(input_url):
    parsed_url = urlparse(input_url)

    normalized_scheme = parsed_url.scheme.lower()
    normalized_host = parsed_url.hostname.lower()

    normalized_url = urlunparse(
        (normalized_scheme, normalized_host, parsed_url.path,
         parsed_url.params, parsed_url.query, parsed_url.fragment)
    )
    return normalized_url


def validate_url(input_url):
    errors_stack = []

    if len(input_url) > 255:
        errors_stack.append('Введенный URL превышает длину в 255 символов')
    elif not input_url:
        errors_stack.append('URL обязателен для заполнения')
    elif not url_validator(input_url):
        errors_stack.append('Введенный URL некорректен ')

    return errors_stack
