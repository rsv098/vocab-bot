import schedule
import time
from main import run_daily_job

schedule.every().day.at("10:00").do(run_daily_job)

while True:
    schedule.run_pending()
    time.sleep(60)
