import requests
from ovos_plugin_manager.templates.ocp import OCPStreamExtractor
from ovos_utils.log import LOG


class OCPPlaylistExtractor(OCPStreamExtractor):

    def validate_uri(self, uri):
        """ return True if uri can be handled by this extractor, False otherwise"""
        return "pls" in uri or ".m3u" in uri

    def extract_stream(self, uri):
        """ return the real uri that can be played by OCP """
        return self.get_playlist_stream(uri)

    @staticmethod
    def get_playlist_stream(uri):
        # .pls and .m3u are not supported by gui player, parse the file
        txt = requests.get(uri).text
        for l in txt.split("\n"):
            if l.startswith("http"):
                return {"uri": l}
        return {"uri": uri}

