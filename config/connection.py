URL_PROXY_CHECK = 'https://api.ipify.org/'
SESSION_PATH = 'data/'

URL_BASE, URL_PICT = '', ''

HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'none',
	'Sec-Fetch-User': '?1'
}

HEADERS_DOWNLOADER = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
	'Accept': 'image/avif,image/webp,*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'cross-site',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache',
	'TE': 'trailers',
	'Upgrade-Insecure-Requests': '1'
}

HEADERS_ASYNC = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Cookie': 'PHPSESSID=b5d91e4955bb8f0bd6420dff8d66859c; wpdiscuz_hide_bubble_hint=1',
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'none',
	'Sec-Fetch-User': '?1',
	'If-Modified-Since': 'Mon, 16 May 2022 12:42:19 GMT',
	'Cache-Control': 'max-age=0',
	'TE': 'trailers'
}
