
import requests,subprocess,platform,time,tg

command = "sudo journalctl -u stationd --no-hostname -o cat --since '1.5 min ago'"

vpsname = platform.node()

def monitor_stationd():
    output = subprocess.check_output(command, shell=True, text=True)

    message = f"On {vpsname} Stationd log is:{output}\n"

    url = f"https://api.telegram.org/bot{tg.TOKEN}/sendMessage?chat_id={tg.chat_id}&text={message}"

    print(requests.get(url).json()) 


while True:
    try:
        monitor_stationd()
    except Exception as e:
        print("An error occurred:", e)

    time.sleep(3600)
