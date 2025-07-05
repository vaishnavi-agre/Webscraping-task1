import requests
from bs4 import BeautifulSoup

url = "https://www.sandipuniversity.edu.in/engineering-technology/school-of-engineering-technology.php"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Programs are listed under <ul> tags in the "Programs Offered" section
    programs = []
    for ul in soup.find_all("ul"):
        for li in ul.find_all("li"):
            text = li.get_text(strip=True)
            if "B.Tech" in text or "M.Tech" in text or "Master" in text:
                programs.append(text)

    if programs:
        for prog in programs:
            print(prog)
    else:
        print("No programs found in <ul> lists.")
else:
    print("Failed to retrieve page.")
