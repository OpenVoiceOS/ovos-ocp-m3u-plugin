import unittest
from unittest.mock import patch, MagicMock

from ovos_ocp_m3u_plugin import OCPPlaylistExtractor
from ovos_ocp_m3u_plugin.config import OCPPlaylistExtractorConfig


class TestOCPPlaylistExtractor(unittest.TestCase):
    def test_supported_seis(self):
        self.assertIn("m3u", OCPPlaylistExtractor.supported_seis)
        self.assertIn("pls", OCPPlaylistExtractor.supported_seis)

    def test_validate_uri(self):
        ext = OCPPlaylistExtractor()
        self.assertTrue(ext.validate_uri("http://example.com/list.m3u"))
        self.assertTrue(ext.validate_uri("http://example.com/list.pls"))
        self.assertFalse(ext.validate_uri("http://example.com/song.mp3"))

    @patch("ovos_ocp_m3u_plugin.requests.get")
    def test_extract_stream_picks_first_http_line(self, mock_get):
        resp = MagicMock()
        resp.text = "#EXTM3U\n#EXTINF:0\nhttp://stream.example.com/live\n"
        mock_get.return_value = resp
        ext = OCPPlaylistExtractor()
        self.assertEqual(
            ext.extract_stream("http://example.com/list.m3u"),
            {"uri": "http://stream.example.com/live"},
        )

    @patch("ovos_ocp_m3u_plugin.requests.get")
    def test_extract_stream_falls_back_to_original_uri(self, mock_get):
        resp = MagicMock()
        resp.text = "#EXTM3U\n#EXTINF:0\n"
        mock_get.return_value = resp
        ext = OCPPlaylistExtractor()
        uri = "http://example.com/list.m3u"
        self.assertEqual(ext.extract_stream(uri), {"uri": uri})


class TestConfig(unittest.TestCase):
    def test_config_is_dict(self):
        self.assertIsInstance(OCPPlaylistExtractorConfig, dict)
        self.assertIn("m3u", OCPPlaylistExtractorConfig)


if __name__ == "__main__":
    unittest.main()
