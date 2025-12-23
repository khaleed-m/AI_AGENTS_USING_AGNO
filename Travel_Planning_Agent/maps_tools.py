#import HTTPX and toolkit from Agno-tools
try:
    import httpx
except ImportError:
    raise ImportError("The 'httpx' module is required. Run 'pip install httpx' to install the library.")

from agno.tools import Toolkit

#to make request calls and convert function to Agno-speecific toolkit.
#Create a Google Maps Tool class that extends the Toolkit class from Agno-tools
#Toolkit is a base class for creating tools that can be used within the Agno framework.
#Api key is passed to the constructor to authenticate requests to the Google Maps API.
class GoogleMapsTool(Toolkit):
    #use the init method to store the api key and define the base url for the Google Maps API.
    def __init__(self, api_key: str):
        super().__init__(name='google_maps_tool')
        self.api_key = api_key
        self.base_url = 'https://maps.googleapis.com/maps/api'

        self.register(self.get_place_maps_url)#Forget to mention you need to use the register method from Toolkit for agents to recognize the function as a tool. 

    def get_place_maps_url(self, place_name: str) -> str:
        """
        Get the Google Maps URL for a specific place using the place name.

        Args:
            place_name (str): The name of the place to search for.

        Returns:
            str: The Google Maps URL for the place.
        """
        search_endpoint = f'{self.base_url}/place/textsearch/json'
        params = {
            'query': place_name,
            'key': self.api_key,
            'fields': 'place_id'
        }

        try:
            response = httpx.get(search_endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            if 'results' in data:
                place_id = data['results'][0]['place_id']

                # Create a Google Maps URL using the place_id
                maps_url = f'https://www.google.com/maps/place/?q=place_id:{place_id}'
                return maps_url

        except httpx.HTTPStatusError as e:
            return f"HTTP error occurred: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
