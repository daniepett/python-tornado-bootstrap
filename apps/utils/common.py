# coding: utf-8
from datetime import datetime
import re
import unicodedata


def smart_split(text, comma=','):
    if isinstance(text, (str, unicode)):
        text = text.strip()
        text = text.split(comma)
        text = map(lambda x: x.strip(), text)
        text = filter(str, text)
        text = list(set(text))
    return text


def to_lower_case(text):
    if text:
        if isinstance(text, (str, unicode)):
            text = text.lower()
        elif isinstance(text, (list, set)):
            text = map(lambda x: x.lower(), text)
    return text


def taggify(text_or_list, comma=','):
    a_list = smart_split(text_or_list, comma=comma)
    a_list = to_lower_case(a_list)
    if a_list and isinstance(a_list, (list, set)):
        a_list = map(lambda x: x.strip(), a_list)
        a_list = filter(str, a_list)
        a_list = list(set(a_list))
    return a_list


#http://refactormycode.com/codes/675-camelcase-to-camel-case-python-newbie
def space_out_camel_case(str_as_camel_case, join=' '):
    """Adds spaces to a camel case string.  Failure to space out string returns the original string.
    >>> space_out_camel_case('DMLSServicesOtherBSTextLLC')
    'DMLS Services Other BS Text LLC'
    """
    if str_as_camel_case is None:
        return None
    pattern = re.compile('([A-Z][A-Z][a-z])|([a-z][A-Z])')
    return pattern.sub(lambda m: m.group()[:1] + join + m.group()[1:], str_as_camel_case)


STRIP_REGEXP = re.compile(r'[^\w\s-]')
HYPHENATE_REGEXP = re.compile(r'[-\s]+')
def slugify(value):
    if not value:
        return value
    if not isinstance(value, unicode):
        value = unicode(value, encoding='utf-8', errors='ignore')
    value = space_out_camel_case(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(STRIP_REGEXP.sub('', value).strip().lower())
    value = HYPHENATE_REGEXP.sub('-', value)
    value = re.sub('-{2,}', '-', value)
    return value


def slugify_with_date(value):
    if not value:
        return value
    value = slugify(value)
    return datetime.today().strftime('%Y-%m-%d') + '-' + value
