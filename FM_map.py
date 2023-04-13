import folium

class Map(folium.Map):

    def __init__(self, location = [35.9969, -83.9978], zoom_start = ) -> None:
        super().__init__()
