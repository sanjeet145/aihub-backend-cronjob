import requests
import datetime

def main():
    print("Cron job running at", datetime.datetime.now())
    try:
        r = requests.get("http://aihub-authentication.onrender.com/api/cronjob/")
        print("Ping response:", r.status_code)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
