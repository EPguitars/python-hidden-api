import logging

from sqlmodel import Session, select
from rich import print
import matplotlib.pyplot as plt

from db_config import engine, ScrapingSession

# PREPARE DATA FOR VISUALIZATION

data = dict()
items_scraped = 0

with Session(engine) as session:
    statement = select(ScrapingSession)
    scraping_sessions = session.exec(statement).all()
    
    previous_day = scraping_sessions[0].date.day

    for session in scraping_sessions:
        day = session.date.day
        month = session.date.month
        year = session.date.year
        formated_date = f"{day}.{month}.{year}"

        if previous_day == day:
            items_scraped += session.items_scraped
            data[formated_date] = items_scraped
        elif previous_day < day:
            previous_day = day
            formated_date = f"{day}.{month}.{year}"
            items_scraped = 0
            items_scraped += session.items_scraped
            data[formated_date] = items_scraped
        else:
            logging.error("Impossible date!")

# VISUALIZE

keys = data.keys()
values = data.values()
plt.bar(keys, values)
plt.xlabel("Dates")
plt.ylabel("Daily scraping traffic")
plt.title("Statistics of Discount One scraping service")
plt.show()