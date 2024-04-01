import requests
import time

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Application is UP"
        else:
            return f"Application is DOWN with status code: {response.status_code}"
    except requests.ConnectionError:
        return "Failed to connect to the application"

if __name__ == "__main__":
    #the url of the application which we want to check
    application_url = "https://www.google.com"  
    while True:
        status = check_application_status(application_url)
        print(f"{time.ctime()}: {status}")
        time.sleep(60) 
