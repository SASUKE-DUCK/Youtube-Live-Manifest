import argparse
import requests

parser = argparse.ArgumentParser(description="Get YouTube video manifest URLs")
parser.add_argument("-url", help="YouTube URL", required=True)

args = parser.parse_args()
youtube_url = args.url

video_id = youtube_url.split('v=')[1]

headers = {
    'origin': 'https://www.youtube.com',
    'referer': 'https://www.youtube.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
}

params = {
    'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
}

json_data = {
    'context': {
        'client': {
            'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36,gzip(gfe)',
            'clientName': 'WEB',
            'clientVersion': '2.20231101.05.00',
        },
    },
    'videoId': video_id,
}

response = requests.post('https://www.youtube.com/youtubei/v1/player', params=params, headers=headers, json=json_data)

response_data = response.json()
dash_manifest_url = response_data['streamingData']['dashManifestUrl'] if 'streamingData' in response_data and 'dashManifestUrl' in response_data['streamingData'] else None
hls_manifest_url = response_data['streamingData']['hlsManifestUrl'] if 'streamingData' in response_data and 'hlsManifestUrl' in response_data['streamingData'] else None

print("DASH Manifest URL:", dash_manifest_url)
print("HLS Manifest URL:", hls_manifest_url)
