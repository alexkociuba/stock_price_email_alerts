from apis import *
import smtplib


print(f"Yesterday's stock price close: {yday_closing_price}")
print(f"Day before yesterday price: {day_before_closing_price}")
difference = (float(yday_closing_price) - float(day_before_closing_price))
percent_move = float(difference) / float(yday_closing_price) * 100
percent_change = f"{round(percent_move, 2)}%"


formatted_string = f"There has been a {percent_change} change in {STOCK_NAME}, here are some recent news articles: " \
                   f"\n\t{article_one}, \n\t{article_two}\n\t{article_three}"

print(formatted_string)

def send_email_alert():
    """This function was made for my Yahoo test account"""

    my_email = "python.testing1112@yahoo.com"
    password = "XXXXXXXXXXXXXXXXX"

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="python.testing9999@gmail.com",
                            msg=f"Subject: Stock Alert: {alphavantage_stock_params['symbol']}."
                                f"\n\nStock price alert for {alphavantage_stock_params['symbol']}.\n{formatted_string}")



# SEND E-MAIL ALERT
# if percent_move >= 1:
#     send_email_alert()
#     print('email was sent')
# else:
#     print("percent move less than 1%")

