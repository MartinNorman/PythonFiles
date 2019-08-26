import requests
import codecs
import datetime
from local_paths import output
from local_paths import output_error
from local_paths import input
vDate = datetime.datetime.now().strftime("%Y-%m-%d")

# Funds
Nav = codecs.open(output + '/' + 'Nav' + vDate + '.txt', 'w', 'utf-8')
texttowrite = 'ID@ISIN@NAV@NAVDATE'
Nav.write(texttowrite + '\r\n')

# Funds with errors
ErrorID = codecs.open(output_error + '/' + 'Error' + vDate + '.txt', 'w', 'utf-8')
texttowrite = 'ID@ERROR'
ErrorID.write(texttowrite + '\r\n')

# Get IDs to read
f = open(input + '/' + 'ID.txt', mode='r', encoding='utf-8')
for x in f:
    print(x)
    static = "https://www.avanza.se/_cqbe/fund/guide/"
    res = requests.get(static + x.strip())
    x_stripped = x.strip()
    res2 = res.json()
    print(res2)
    try:
        isin = res2["isin"]
        print(isin)
        nav = res2["nav"]
        print(nav)
        navDate = res2["navDate"]
        print(navDate)
        # Write to file
        Nav.write("%s" % x_stripped + "@" + "%s" % isin + "@" + "%s" % nav + "@" + "%s" % navDate + '\r\n')
    except Exception as e:
        ErrorID.write("%s" % x_stripped  + "@" + "%s" % str(e) + '\r\n')