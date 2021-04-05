import datetime


if __name__ == '__main__':
    #user = fake_useragent.UserAgent(use_cache_server=False)
    '''
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    link = 'https://www.sciencedaily.com/releases/2021/01/210107112418.htm'
    response = requests.get(link, headers = header)
    soup = BeautifulSoup(response.text,'html.parser')
    t = soup.find('div',id = 'text').text
    print(t)
    
    response = requests.get('https://www.nytimes.com/2021/01/05/science/corona-satellites-environment.html')
    #soup = BeautifulSoup(response.text, 'lxml')
    soup = BeautifulSoup(response.text, 'html.parser')
    #div class="css-53u6y8" soup.find_all("p", class_="css-axufdj evys1bk0")
    text = soup.get_text().split('\n')
    for i in text:
        j = i.replace(' ','')
        res.append(j)
    res = list(filter(None, text))
    print(res)
    #link = 'https...'
    #res1 = requests.get(link).text
    if( int(response.status_code)== 200 ):
        print()
        #testblock = soup.find_all("div", class_="css-53u6y8")

        #print(testblock)
    
    print(response.status_code)
    print(response.content)'''

    '''country_list = [["Moscow", "Cheboksary", "Sochi"], ["Paris", "Lyon", "Nice"],
                    ["New York", "Dallas", "San Francisco"]]

    long_cities = [city for country in country_list for city in country if len(city) >= 6]

    double = float(input())
    i = int(input())
    print(f'%.{i}f' % double)'''
    x = float(input())
    if x < 2.0:
        print('Analytic')
    elif 2.0 < x < 3.0:
        print('Synthetic')
    elif x > 3.0:
        print('Polysynthetic')

