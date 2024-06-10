import requests
import os
import re

proxy_sources = [
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://api.openproxylist.xyz/socks5.txt",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
    "https://openproxy.space/list/socks5",
    "https://proxyspace.pro/socks5.txt",
    "https://spys.me/socks.txt",
    "https://raw.githubusercontent.com/AGDDoS/AGProxy/master/proxies/socks5.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks5_proxies.txt",
    "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/socks5/global/socks5_checked.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/im-razvan/proxy_list/main/socks5.txt",
    "https://raw.githubusercontent.com/Master-Mind-007/Auto-Parse-Proxy/main/socks5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
    "https://raw.githubusercontent.com/NotUnko/autoproxies/main/proxies/socks5",
    "https://raw.githubusercontent.com/ObcbO/getproxy/master/file/socks5.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/Sage520/Proxy-List/main/socks5.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/socks5_proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/socks5.txt",
    "https://raw.githubusercontent.com/tuanminpay/live-proxy/master/socks5.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt",
]

proxies = []

def parseProxy():
    global proxies 
    
    print("Получения прокси...")

    for url in proxy_sources:
        try:
            response = requests.get(url)
            response.raise_for_status()
            proxy_lines = response.text.splitlines()
            
            for line in proxy_lines:
                if re.match(r"\d+\.\d+\.\d+\.\d+:\d+", line):
                    proxy = line.split()[0]
                    clean_proxy = proxy.split(':')[0:2]
                    clean_proxy = ":".join(clean_proxy)
                    proxies.append(clean_proxy)
            print(f"Успешно получены прокси из {url}")
                    
        except Exception as e:
            print(f"Ошибка получения прокси из {url}: {e}")
            continue
    
    # Удаления дубликатов
    proxies = list(set(proxies))
    proxies.sort(key=lambda x: tuple(map(int, x.split(':')[0].split('.'))))
    
    # Сохранения прокси в файл
    proxy_file = os.path.join("proxy.txt")
    with open(proxy_file, "w") as file:
        file.write("\n".join(proxies))
        print(f"Прокси были сохранены в файл {proxy_file}.")
    
def getCount():
    return len(proxies)

# Использование 
if __name__ == "__main__":
    parseProxy()
    print(f"Количество прокси: {getCount()}")
    print(f"Прокси были успешно получены и сохранены в файл!")
