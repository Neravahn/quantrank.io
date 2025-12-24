from statsFolder.heatmap import daily_Users
from datetime import datetime

with open("/home/quantrank/QuantRank.io/scheduler.log", "a") as f:
    f.write(f"cron ran at {datetime.now()}\n")
if __name__ == "__main__":
    daily_Users()