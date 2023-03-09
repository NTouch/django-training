class Gif:

    def __init__(self, gif_id: str, gif_title: str, gif_url: str, gif_size: list[str]):
        """
        Gif object base on GIPHY website gif

        :param gif_id: str id from GIPHY
        :param gif_title: str gif title
        :param gif_url: str url of original gif
        :param gif_size: list[str] (height, width) of gif
        """
        self.id = gif_id
        self.title = gif_title
        self.url = gif_url
        self.size = gif_size

    def __repr__(self):
        return f"{self.id} : {self.title}\n{self.url} // {self.size}"