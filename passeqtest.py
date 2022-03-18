# String password sequrity cheking function


import string


def password_seq(value: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    if len(value) < 8:
        return 'Too weak'
    if all(i in digits for i in value) or all(i in lowers for i in value) or all(
            i in uppers for i in value):
        return 'Weak'
    if any(i in digits for i in value) and any(i in lowers for i in value) and any(
            i in uppers for i in value):
        return 'Very good'
    if (any(i in digits for i in value) and any(i in lowers for i in value)) or (
            any(i in digits for i in value) and any(i in uppers for i in value)) or (
            any(i in lowers for i in value) and any(i in uppers for i in value)):
        return 'Good'


if __name__ == '__main__':
    assert password_seq('') == 'Too weak'
    assert password_seq('1234567') == 'Too weak'
    assert password_seq('qwertyu') == 'Too weak'
    assert password_seq('QWERTYU') == 'Too weak'
    assert password_seq('QWERtyu') == 'Too weak'
    assert password_seq('12345678') == 'Weak'
    assert password_seq('QWERTYUI') == 'Weak'
    assert password_seq('qwertyui') == 'Weak'
    assert password_seq('1234567890') == 'Weak'
    assert password_seq('qwertyuiop') == 'Weak'
    assert password_seq('QWERTYUIO') == 'Weak'
    assert password_seq('1234qwer') == 'Good'
    assert password_seq('1234QWER') == 'Good'
    assert password_seq('QWERqwer') == 'Good'
    assert password_seq('12345QWER') == 'Good'
    assert password_seq('1234qwert') == 'Good'
    assert password_seq('QWERqwer') == 'Good'
    assert password_seq('123QWEqw') == 'Very good'
    assert password_seq('123456Qa') == 'Very good'
    assert password_seq('QWERqwe1') == 'Very good'
    assert password_seq('QWEewq1123') == 'Very good'
