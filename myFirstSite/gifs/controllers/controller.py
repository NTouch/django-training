import os.path

from ..data import constant
from ..model.gif import Gif

from .helper import *


class AppController:
    def __init__(self) -> object:
        """
        AppController object
        """
        self.gifs = []

    def query_gifs(self, user_query: str) -> list[Gif]:
        query = format_for_url(user_query)
        number_of_results = 5

        # create url compatible with GIPHY API
        url = create_query_url(constant.URL_GIPHY, constant.API_KEY,
                                       query, number_of_results)

        # results of query in JSON
        url_response = http_request(url).json()

        self.create_gif(url_response["data"])

        return self.gifs

    def create_gif(self, gifs: dict) -> None:
        """
        instantiate Gif model for every gifs

        :param gifs: dict need ["id"],
                                ["title"],
                                ["url"],
                                (["height"], ["width"])
        :return: None
        """
        for gif in gifs:
            self.gifs.append(Gif(gif["id"], gif["title"], gif["embed_url"], {'height': gif["images"]["original"]["height"], 'width': gif["images"]["original"]["width"]}))
