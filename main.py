from bot_class import InstaBot


def main():
    try:
        want_continue = ''
        while want_continue != 'n':
            name = input('Введіть логін аккаунту: ')
            password = input('Введіть пароль від аккаунту: ')

            bot = InstaBot(name, password)
            bot.login()
            lst = bot.make_list()

            print(lst)

            if input('Чи бажаєте зробити список виключень? [y - Yes], [n - No]: ').strip().lower() == 'y':
                exclusion = set(['https://www.instagram.com/' + i.strip() +'/' for i in input('Введіть назви аккаутів, від яких не треба відписуватися через ";" (без лапок): ').split(';')])
                lst = set(lst) - exclusion
                bot.unsubscribe(lst)

            else:
                bot.unsubscribe(lst)
                
            bot.close_youreself()
            want_continue = input('Чи бажаєте продовжити? [y - Yes][n - No]: ')

        print('Програма розумної відписки завершилася\nГарного дня :)')
    
    except Exception as e:
        print('Виникла помилка:\n\n')
        print(e)


if __name__ == '__main__':
    main()