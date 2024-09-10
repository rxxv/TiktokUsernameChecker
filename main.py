import requests
from bs4 import BeautifulSoup
import random
import string
from concurrent.futures import ThreadPoolExecutor, as_completed
from fake_useragent import UserAgent
import time
from colorama import Fore, Style, init

init(autoreset=True)

def read_proxies_from_file():
    try:
        with open('proxies.txt', 'r') as file:
            proxies = [line.strip() for line in file if line.strip()]
            print(f"[+] Loaded {len(proxies)} proxies from proxies.txt")
            return proxies
    except FileNotFoundError:
        print("[×] proxies.txt file not found.")
        return []

def get_random_proxy(proxies):
    return random.choice(proxies)

def save_available_username(username):
    with open("available.txt", "a") as file:
        file.write(f"{username}\n")

def check_username_availability(username, use_proxies=False, proxies=None):
    random_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    
    headers = {
        "Host": "www.tiktok.com",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "upgrade-insecure-requests": "1",
        "user-agent": random_user_agent,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-language": "en-US,en;q=0.9"
    }
    # The rest of your function remains the same
    
    for _ in range(3):
        try:
            if use_proxies and proxies:
                proxy = get_random_proxy(proxies)
                proxies_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
                response = requests.get(f'https://www.tiktok.com/@{username}', headers=headers, proxies=proxies_dict, timeout=5)
            else:
                response = requests.get(f'https://www.tiktok.com/@{username}', headers=headers, timeout=5)
            
            if response.status_code != 200:
                return f"[×] Failed to retrieve data for username: {username} (status code {response.status_code})"
            
            soup = BeautifulSoup(response.text, 'html.parser')
            user_data_script = None
            for script in soup.find_all('script'):
                if 'userInfo' in script.text:
                    user_data_script = script.string
                    break
            
            if not user_data_script:
                save_available_username(username)
                return f"{Fore.GREEN}[✓] '{username}' is available!{Style.RESET_ALL}"
            else:
                return f"{Fore.RED}[×] '{username}' is already taken.{Style.RESET_ALL}"
        
        except requests.RequestException as e:
            print(f"[×] Request error for username '{username}': {e}")
            time.sleep(1)
    return f"[×] Failed to check username '{username}' after multiple attempts."

def generate_random_usernames(count, length):
    usernames = []
    for _ in range(count):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        usernames.append(username)
    return usernames

def read_usernames_from_file():
    try:
        with open('usernames.txt', 'r') as file:
            usernames = [line.strip() for line in file if line.strip()]
            print(f"[+] Loaded {len(usernames)} usernames from usernames.txt")
            return usernames
    except FileNotFoundError:
        print("[×] usernames.txt file not found.")
        return []

def check_usernames_with_workers(usernames, use_proxies, proxies):
    total_usernames = len(usernames)
    start_time = time.time()
    checked_usernames = 0
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(check_username_availability, username, use_proxies, proxies): username for username in usernames}
        
        for future in as_completed(futures):
            result = future.result()
            print(result)
            checked_usernames += 1
            elapsed_time = time.time() - start_time
            if elapsed_time > 0:
                cpm = (checked_usernames / elapsed_time) * 60
                print(f"CPM: {cpm:.2f} ({checked_usernames}/{total_usernames}) usernames checked.")

print('Tiktok Usernames Checker by @rxxv')
def main():
    use_proxies = input('[+] Use proxies? (yes/no): ').strip().lower() == 'yes'
    
    proxies = []
    if use_proxies:
        proxies = read_proxies_from_file()
        if not proxies:
            print("[×] No proxies available. Exiting.")
            return

    source = input('[+] Read usernames from a file or generate random ones? (file/random): ').strip().lower()

    if source == 'file':
        usernames = read_usernames_from_file()
        if not usernames:
            print("[×] No usernames found in file. Exiting.")
            return
    else:
        num_usernames = int(input('[+] How many usernames do you want to generate: '))
        num_characters = int(input('[+] How many characters: '))
        usernames = generate_random_usernames(num_usernames, num_characters)
    
    check_usernames_with_workers(usernames, use_proxies, proxies)

if __name__ == "__main__":
    main()
