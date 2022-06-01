import requests
from bs4 import BeautifulSoup

def get_person(person:str):
    """
    Gets a person from wikipedia
    """
    person = person.replace(" ","_")
    
    r = requests.get("https://en.wikipedia.org/wiki/" + person)
    soup = BeautifulSoup(r.text, "lxml")
    
    birthplace = soup.find("div", class_="birthplace")
    bday = soup.find_all("span", class_="bday")
    