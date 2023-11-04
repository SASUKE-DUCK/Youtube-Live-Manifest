# Youtube-Live-Manifest

This Python script allows you to extract the DASH and HLS manifest URLs of a YouTube video from its URL. These manifest URLs can be used for various purposes, such as streaming the video or extracting different resolutions and codecs.

## Usage

1. Make sure you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Open your terminal and navigate to the repository's directory.
4. Run the script with the following command, replacing `urlyoutube` with the URL of the YouTube video you want to analyze:

```bash
python main.py -url urlyoutube
```

The script will retrieve and display the DASH and HLS manifest URLs.

## Recommendation

I recommend using the DASH manifest as it provides access to a wider range of resolutions and codecs compared to HLS. The HLS manifest can sometimes be limited to 1080p. Here is a clear example of the available resolutions and codecs for DASH and HLS:

## DASH:

![image](https://cdn.discordapp.com/attachments/852144117923184640/1170385832314687622/image.png?ex=6558d9bf&is=654664bf&hm=35102a0f3403046490f26faed6d0fa6a23b3f054d8518bfd4214412895b9202f&)


## HLS:

![image](https://cdn.discordapp.com/attachments/852144117923184640/1170385773284049077/image.png?ex=6558d9b1&is=654664b1&hm=80300801617fa8853ce7b6133a665c89cb6ccab4d40ddef40903855bd5352ee0&)


The test video used for this example was the first live video encountered when opening YouTube.

> **Warning**
>
> I'm only uploading this for educational.

## Disclaimer

Please note that the script's functionality relies on the current structure of YouTube's website and API, which may change over time. The use of this script must comply with YouTube's terms of service and policies.

If you encounter any issues or have suggestions for improvements, feel free to create an issue or a pull request.

---

**Note:** This script is for educational and personal use only. Downloading and redistributing copyrighted content without proper authorization may violate YouTube's terms of service and local copyright laws.
```
