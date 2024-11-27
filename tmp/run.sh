#set proxy
export https_proxy=http://127.0.0.1:1080

#download raw data
#质量很差
#curl https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks5/data.txt -o socks5.txt
#curl https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks4/data.txt -o socks4.txt
#curl https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/http/data.txt -o http.txt
#curl https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/https/data.txt -o https.txt

#质量好
curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt -o socks4.txt 
curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt -o socks5.txt 
curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt -o http.txt

curl https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/http.txt >>http.txt
curl https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks4.txt >> socks4.txt
curl https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks5.txt >> socks5.txt
curl https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/http.txt >>http.txt
curl https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/socks4.txt >>socks4.txt
curl https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/socks5.txt >>socks5.txt

curl https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/http.txt >> http.txt




curl 'https://proxy5.net/wp-admin/admin-ajax.php?action=proxylister_download&nonce=8b12c3524c&format=txt&filter=\{%22protocols%22:%22HTTP%22,%22latency%22:0,%22page_size%22:20,%22page%22:1\}' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'cookie: _ga=GA1.1.1293367504.1732002488; _gcl_au=1.1.1875742973.1732002489; _ym_uid=1732002490428729031; _ym_d=1732002490; _ym_isad=2; _ym_visorc=w; _ga_2ZGKN4M0P5=GS1.1.1732002488.1.0.1732002499.0.0.0' \
  -H 'pragma: no-cache' \
  -H 'priority: u=0, i' \
  -H 'referer: https://proxy5.net/free-proxy' \
  -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'  >>http.txt

curl 'https://proxy5.net/wp-admin/admin-ajax.php?action=proxylister_download&nonce=8b12c3524c&format=txt&filter=\{%22protocols%22:%22SOCKS4%22,%22latency%22:0,%22page_size%22:20,%22page%22:1\}' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'cookie: _ga=GA1.1.1293367504.1732002488; _gcl_au=1.1.1875742973.1732002489; _ym_uid=1732002490428729031; _ym_d=1732002490; _ym_isad=2; _ym_visorc=w; _ga_2ZGKN4M0P5=GS1.1.1732002488.1.0.1732002499.0.0.0' \
  -H 'pragma: no-cache' \
  -H 'priority: u=0, i' \
  -H 'referer: https://proxy5.net/free-proxy' \
  -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'  >>socks4.txt

curl 'https://proxy5.net/wp-admin/admin-ajax.php?action=proxylister_download&nonce=8b12c3524c&format=txt&filter=\{%22protocols%22:%22SOCKS5%22,%22latency%22:0,%22page_size%22:20,%22page%22:1\}' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'cookie: _ga=GA1.1.1293367504.1732002488; _gcl_au=1.1.1875742973.1732002489; _ym_uid=1732002490428729031; _ym_d=1732002490; _ym_isad=2; _ym_visorc=w; _ga_2ZGKN4M0P5=GS1.1.1732002488.1.0.1732002499.0.0.0' \
  -H 'pragma: no-cache' \
  -H 'priority: u=0, i' \
  -H 'referer: https://proxy5.net/free-proxy' \
  -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'  >>socks5.txt

curl  https://api.openproxylist.xyz/http.txt >> http.txt
curl  https://api.openproxylist.xyz/socks4.txt >> socks4.txt
curl  https://api.openproxylist.xyz/socks5.txt >> socks5.txt


curl 'https://fineproxy.org/wp-admin/admin-ajax.php?action=proxylister_download&nonce=286663de32&format=txt&filter=%7B%22protocols%22%3A%22HTTP%22%2C%22latency%22%3A0%2C%22uptime%22%3A0%2C%22last_checked%22%3A%220%22%2C%22trp-form-language%22%3A%22cn%22%2C%22page_size%22%3A20%2C%22page%22%3A1%7D' >>http.txt
curl 'https://fineproxy.org/wp-admin/admin-ajax.php?action=proxylister_download&nonce=286663de32&format=txt&filter=%7B%22protocols%22%3A%22HTTPS%22%2C%22latency%22%3A0%2C%22uptime%22%3A0%2C%22last_checked%22%3A%220%22%2C%22trp-form-language%22%3A%22cn%22%2C%22page_size%22%3A20%2C%22page%22%3A1%7D' >>https.txt
curl 'https://fineproxy.org/wp-admin/admin-ajax.php?action=proxylister_download&nonce=286663de32&format=txt&filter=%7B%22protocols%22%3A%22SOCKS4%22%2C%22latency%22%3A0%2C%22uptime%22%3A0%2C%22last_checked%22%3A%220%22%2C%22trp-form-language%22%3A%22cn%22%2C%22page_size%22%3A20%2C%22page%22%3A1%7D' >>socks4.txt
curl 'https://fineproxy.org/wp-admin/admin-ajax.php?action=proxylister_download&nonce=286663de32&format=txt&filter=%7B%22protocols%22%3A%22SOCKS5%22%2C%22latency%22%3A0%2C%22uptime%22%3A0%2C%22last_checked%22%3A%220%22%2C%22trp-form-language%22%3A%22cn%22%2C%22page_size%22%3A20%2C%22page%22%3A1%7D' >>socks5.txt


curl 'https://api.proxyscrape.com/v4/free-proxy-list/get?request=get_proxies&skip=0&proxy_format=protocolipport&format=text&limit=1500'   -H 'accept: application/json, text/plain, */*'   -H 'accept-language: zh-CN,zh;q=0.9'   -H 'cache-control: no-cache'   -H 'origin: https://proxyscrape.com'   -H 'pragma: no-cache'   -H 'priority: u=1, i'   -H 'referer: https://proxyscrape.com/'   -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"'   -H 'sec-ch-ua-mobile: ?0'   -H 'sec-ch-ua-platform: "Windows"'   -H 'sec-fetch-dest: empty'   -H 'sec-fetch-mode: cors'   -H 'sec-fetch-site: same-site'   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' -o mix.txt



#filter available
python3 proxiesCheckPool.py http.txt
python3 proxiesCheckPool.py socks4.txt
python3 proxiesCheckPool.py socks5.txt
python3 proxiesCheckPool.py mix.txt

#remove duplicate
sort -k 1   ../proxyList/http.txt   | uniq > ../proxyList/http.txt.new
mv ../proxyList/http.txt.new ../proxyList/http.txt
sort -k 1   ../proxyList/https.txt   | uniq > ../proxyList/https.txt.new
mv ../proxyList/https.txt.new ../proxyList/https.txt
sort -k 1   ../proxyList/socks4.txt   | uniq > ../proxyList/socks4.txt.new
mv ../proxyList/socks4.txt.new ../proxyList/socks4.txt
sort -k 1   ../proxyList/socks5.txt   | uniq > ../proxyList/socks5.txt.new
mv ../proxyList/socks5.txt.new ../proxyList/socks5.txt


wc -l ../proxyList/*.txt
