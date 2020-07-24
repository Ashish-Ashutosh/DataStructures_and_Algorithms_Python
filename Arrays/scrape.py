import requests
from lxml import html

#login
#pass
USERNAME = "mages"
PASSWORD = "ma#22.04."
STUDIENFACH = "20433"

LOGIN_URL = "https://ww2.uni-assist.de/portal/"
URL = "https://ww2.uni-assist.de/portal/index.php?go=sea"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    #tree = html.fromstring(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "login": USERNAME,
        "pass": PASSWORD
        #"csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))

    # Scrape url

    payload = {
        "stg": STUDIENFACH,

    }
    #retrieve web page with our data and parse using html and save in tree
    # result = session_requests.get(URL, headers=dict(referer=URL))
    # print(result.content)

    result = session_requests.post(URL, data=payload)
    print(result.content)

    #tree = html.fromstring(result.content)





    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")


if __name__ == '__main__':
    main()