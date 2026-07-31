# OCP m3u Plugin

This plugin is a stream extractor for [OVOS Common Play (OCP)](https://github.com/OpenVoiceOS/ovos-media). It lets OCP play `.m3u` and `.pls` playlist URLs. OCP media players cannot read these playlist formats directly, so the plugin fetches the playlist and returns the first playable stream URL inside it.

## Install

```bash
pip install ovos-ocp-m3u-plugin
```

## Usage

OCP loads this plugin through its extractor entry points. No manual setup is needed once the package is installed.

The plugin handles any stream URI in the form `{sei}//{uri}`, where `{sei}` is `m3u` or `pls`. It also handles plain URLs that contain `.m3u` or `pls`.

## Related projects

- [OpenVoiceOS/ovos-media](https://github.com/OpenVoiceOS/ovos-media), the OCP media player that consumes this plugin.
- [OpenVoiceOS/ovos-ocp-audio-plugin](https://github.com/OpenVoiceOS/ovos-ocp-audio-plugin), a sibling OCP audio extractor plugin.
- [OpenVoiceOS/ovos-ocp-news-plugin](https://github.com/OpenVoiceOS/ovos-ocp-news-plugin), a sibling OCP stream extractor plugin.

## License

Apache-2.0
