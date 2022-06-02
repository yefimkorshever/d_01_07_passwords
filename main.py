import urwid


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(character.isdigit() for character in password)


def has_letters(password):
    return any(character.isalpha() for character in password)


def has_upper_letters(password):
    return any(character.isupper() for character in password)


def has_lower_letters(password):
    return any(character.islower() for character in password)


def has_symbols(password):
    return any(not character.isdigit() and
               not character.isalpha() for character in password)


def on_ask_change(edit, password, reply):
    checks = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    score = 0
    add_score = 2
    for check in checks:
        if check(password):
            score += add_score

    reply.set_text("Рейтинг пароля: %s" % score)


def main():
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change, reply)
    urwid.MainLoop(menu).run()


if __name__ == '__main__':
    main()
