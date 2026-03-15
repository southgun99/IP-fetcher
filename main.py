import requests

def get_ip_info(ip=None):
    """
    Fetches IP information using the ipapi.co free API.
    If no IP is provided, it returns info about your own IP.
    """

    url = f"https://ipapi.co/{ip}/json/" if ip else "https://ipapi.co/json/"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            return {"error": data.get("reason", "Unknown error")}

        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country_name"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "timezone": data.get("timezone"),
            "org": data.get("org"),
        }

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    print("Fetching your IP info...")
    info = get_ip_info()
    print(info)
