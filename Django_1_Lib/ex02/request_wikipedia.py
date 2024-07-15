import sys, dewiki, requests

def request_wikipedia(page: str):
    url = f"https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": page,
        "format": "json",
        "prop": "wikitext",
        "redirects": "true"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "error" in data:
            raise Exception(data["error"]["info"])
        return dewiki.from_string(data["parse"]["wikitext"]["*"])
    except  requests.HTTPError as e:
        raise SystemExit(f"HTTP error occurred: {e}")
    except Exception as e:
        raise SystemExit(f"❌ An error occurred: {e}")

def main():
    if len(sys.argv) == 2:
        try:
            wiki = request_wikipedia(sys.argv[1])
            with open(f"{sys.argv[1].replace(' ', '_')}.wiki", "w") as file:
                file.write(wiki)
        except Exception as e:
            print(f"❌ An error occurred: {e}")
    else:
        print("❌ Usage: python3 request_wikipedia.py <page>")

if __name__ == "__main__":
    main()
