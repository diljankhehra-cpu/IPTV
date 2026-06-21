import requests

def update_list():
    url = "https://iptv-org.github.io/api/streams.json"
    response = requests.get(url)
    data = response.json()

    with open("in.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for item in data:
            if item.get("country") == "in":
                f.write(f"#EXTINF:-1,{item.get('title', 'Channel')}\n")
                f.write(f"{item.get('url')}\n")

if __name__ == "__main__":
    update_list()
