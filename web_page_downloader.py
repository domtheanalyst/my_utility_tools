import requests
from pathlib import Path

def web_saver(url:str, filename:str) -> str:

    if not filename.endswith(".html"):
        filename += ".html"
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0"
    }

    try:
        # using timeout 
        response = requests.get(url, headers=headers, timeout=10)
        #raise http error
        response.raise_for_status()

        # saving downloaded file
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        # Get the absolute path of the saved file
        file_path = Path(filename).resolve()
        return f"Download completed! You can find the file here {file_path}"

    except requests.exceptions.RequestException as e:
        return f"Download failed. Error: {e}" 


if __name__ == "__main__":

    url = input("Enter Link Here: ".upper())
    clean_url = url.strip().encode('ascii', 'ignore').decode('ascii')
    save_as = input("Enter the name you want the file to be saved as: ".upper())

    result = web_saver(clean_url, save_as)

    print(result)
    