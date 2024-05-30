import os
import time
import requests
import asyncio
import dotenv

env = dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")

async def rhyme_finder(word):
        print("Rhyming Started")
        url = f"https://rhyming.ir/api/rhyme-finder?api={API_KEY}&w={word}&sb=1&mfe=2&eq=1"
        response = requests.request("GET", url)
        print("Rhyming Ended")
        return  response.json()

def get_states():
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.get(url,verify=False)
    print(response)
    return response.json()

def get_cities(id):
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={id}"
    response = requests.get(url,verify=False)
    return response.json()

async def get_coordinates(state_name, city_name):
    print("Coordinates Started")
    states = get_states()
    for state in states:
        if state["name"] == state_name:
            response = get_cities(state["id"])
            cities = response["cities"]
            for city in cities:
                if city["name"] == city_name:
                    latitude = city["latitude"]
                    longitude = city["longitude"]
                    break
            else:
                print(f"شهری به نام {city_name} نشد")
                latitude = None
                longitude = None
            break
    else:
        print(f"استانی با نام {state_name} پیدا نشد")
        latitude = None
        longitude = None

    print("Coordinates Ended")
    return latitude, longitude

    
async def main():
    print("Process Started")
    result = await asyncio.gather(rhyme_finder("مادر"), get_coordinates("اصفهان","اصفهان"))
    print(result)
    


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time:0.2f} seconds.")