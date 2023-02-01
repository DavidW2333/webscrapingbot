from Booking.booking import Booking
try:
    with Booking() as bot:
        bot.get_firstPage()
        bot.select_place("Auckland")
        bot.select_dates('11/02/2023', "16/02/2023")
        bot.select_num_guests(5)
        bot.search()
        bot.apply_filtration()
        bot.report_results()

except Exception as e:
    print("There is an issue here")