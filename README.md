# TikTok Usernames Checker by @rxxv

This script checks the availability of TikTok usernames either by reading from a file or generating random usernames. It uses multithreading (3 threads) to speed up the checking process and supports the use of proxies to prevent rate limiting and better cpm.

## Features
- **Proxy Support**: You can use proxies by add the proxy list in the `proxies.txt` file. If you don't want to use proxies, the script can run without them (proxyless) but need a good vpn for better cpm.
- **Multithreading**: The script uses 3 threads to process usernames in parallel.

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rxxv/TiktokUsernameChecker.git
   cd TiktokUsernameChecker
   ```

2. **Install Required Packages**:
   Make sure you have the required Python packages installed:
   ```bash
   pip install -r requirements.txt
   ```
   The key packages are:
   - `requests`
   - `beautifulsoup4`
   - `fake-useragent`
   - `colorama`

3. **Create a Proxies File** *(optional)*:
   If you want to use proxies, create a file named `proxies.txt` in the same directory as the script. Add one proxy per line in the format `ip:port` (e.g., `123.45.67.89:8080`).

4. **Run the Script**:
   Start the script and choose whether you want to use proxies or run proxyless:
   ```bash
   python main.py
   ```

   - The script will ask whether you want to use proxies.
   - It will then ask if you want to load usernames from a file (`usernames.txt`) or generate random ones.
   - The available usernames will be saved in `available.txt`.

## Example Output

Here’s an example of how the script works:

![Tiktok Username Checker Example](https://i.imgur.com/zzfMyZh.jpeg)

In this example, we checked 20 randomly generated usernames with 4 characters each. The script shows color-coded output:
- **Green**: Username is available.
- **Red**: Username is already taken.

The script also reports **CPM** (Checks Per Minute) to give an idea of the speed.

## Important Notes

- **VPN Usage**: It’s highly recommended to use a VPN when running this script. I personally use **ExpressVPN** and achieve around **200 CPM** (checks per minute).
  
  If you don't use a VPN, your requests might get blocked by TikTok servers after a while, especially when using a lot of proxies.

- **Doesn't Check Banned Users**: This script doesn’t check whether a username is banned by TikTok. It simply checks if a username is available or taken based on profile existing.

- **Low Probability of Finding Available Usernames**: The chances of finding available usernames are **low** since TikTok is a very popular platform. Finding available usernames depends largely on **luck**, and generating random usernames might yield poor results.

- **CPM**: The CPM (Checks Per Minute) can vary based on your internet speed, proxies, and VPN. I achieved around **200 CPM** using ExpressVPN with this script.

## License

This project is licensed under the MIT License.
