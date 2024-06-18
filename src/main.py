#!bin/env python


import requests as r
import json
def main():

    url = 'https://parseapi.back4app.com/classes/Country?limit=10&include=continent&keys=name,capital,continent,continent.name'
    

    headers = {
        'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja',
    'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH'}
    
    try:
        response = r.get(url, headers=headers)

        if response.status_code == 200:
            response = response.json()
            
        else:
            print('Error: ', response.status_code)
            return None

    except requests.exceptions.RequestException as b:
        print('Error: ', b)
        return None


    continent_count = {"North America": 0, "South America": 0, "Europe": 0, "Africa": 0, "Asia": 0, "Antarctica": 0, "Australia": 0, "Oceania": 0}
    print(f" number of countries: {len(response['results'])}")
    for country in response['results']:
        continent_count[country['continent']['name']] += 1
    print("Continent Count: ", continent_count.items())

    # country_info = open('countries.json', 'w')                              #
    # country_info.write(f"{json.dumps(continent_count, indent=2)}")          #
    # country_info.close()                                                    #
    #                                                                         #
    # country_count = {'name': 0}                                             #
    # print(f"number of countries with letter y: {len(response['results'])}") #
    # for countries in response['results']:                                   #
    #                                                                   #
        # if countries['name'] += 1                             #
    #                                                           #
    # print("countries with letter y:", country_count.items())  #
    #                                                           #
    # name_info = open('countries.jason', 'w')                  #
    # name_info.write(f"{json.dumps(country_count, indent=4)}") #
    # name_info.close()                                         #
        
        
    


    

    
    




if __name__ == "__main__":
    main()

