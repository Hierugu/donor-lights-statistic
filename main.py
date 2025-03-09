from bs4 import BeautifulSoup
import requests, csv
import datetime
import sys
# 1+ 1- 2+ 2- 3+ 3- 4+ 4-

def log_message(message):
        with open('script_log.txt', 'a') as log:
            log.write(f"{datetime.datetime.now()}: {message}\n")

try:
    url = "https://donor.mos.ru/donoru/donorskij-svetofor/"

    response = requests.get(url)
    # print(response)

    bs = BeautifulSoup(response.text, 'html.parser')
    lights = bs.find('table', 'donor-svetofor-restyle')
    date = bs.find('div', 'content').p.b.text.split()[-1]
    data = [date]
    # print(lights)

    for light in lights.find_all('tr')[1].find_all('td'):
        # print(light.text, '-', light['class'][0] )
        data.append(light['class'][0])

    with open('donor_lights.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print(data)
    log_message(f"OK {data}")
except Exception as e:
    print("Exception:", e)
    log_message(f"Exception: {e}")


