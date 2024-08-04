"""This module contains functions to scrape ad links from Divar.

Functions:
    get_links(): Gets ad links from divar and saves to urls.csv.
Third party imports:
    webdriver (from selenium)
    By (from selenium.webdriver.common.by)
    NoSuchElementException (from selenium.webdriver.common.exceptions)
    (pip install selenium)
"""

__all__ = ["get_links"]

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# ---------------------------------------------------------------------
def get_links(city: str = "tehran", group: str = "apartment") -> str:
    """Gets ad links from divar and saves to urls.csv.

    Args:
        city (str, default "tehran"): The city to scrape links from.
        group (str, default "apartment"): The group to scrape links from.
    Returns:
        str: A message representing result of function get_links.
    """

    if not _check_arguments(city, group):
        return "Wrong city or group name."

    url = f"https://divar.ir/s/{city}/buy-{group}"
    links_list = _make_links_list(url)

    with open("urls.csv", "w", encoding="utf-8", newline="") as file:
        for link in links_list:
            file.writelines([link + ",\n"])
    return "Done."


# ---------------------------------------------------------------------
def _check_arguments(city: str, group: str) -> bool:
    allowed_cities = [
        "tehran",
        "tabriz",
        "mashhad",
        "isfahan",
        "karaj",
        "shiraz",
        "qom",
        "ahvaz",
        "kermanshah",
    ]
    allowed_groups = ["apartment", "villa", "old-house"]
    if city not in allowed_cities or group not in allowed_groups:
        return False
    return True


# ---------------------------------------------------------------------
def _make_links_list(url: str) -> list:
    browser = webdriver.Chrome()
    browser.get(url)
    flag = True
    links_list = []

    while flag or len(links_list) < 1000:
        # The div containing links for each AD
        selector = "div.post-list__widget-col-c1444 > a"
        link_div = browser.find_elements(By.CSS_SELECTOR, selector)

        for link in link_div:
            link = link.get_attribute("href")
            if link not in links_list:
                links_list.append(link)

        # Little time&Location element in right-bottem of each AD
        selector = (
            "div.kt-post-card__bottom > .kt-post-card__bottom-description"
        )
        bottom_div = browser.find_elements(By.CSS_SELECTOR, selector)

        for info in bottom_div:
            info = info.get_attribute("title")
            if info.startswith(
                (
                    "دیروز",
                    "پریروز",
                    "۳ روز پیش",
                    "۴ روز پیش",
                    "۵ روز پیش",
                    "۶ روز پیش",
                    "۷ روز پیش",
                )
            ):
                flag = False

        new_height, last_height = _scroll(browser)

        if new_height == last_height:
            if not _try_show_more_button(browser):
                flag = False
    return links_list


# ---------------------------------------------------------------------
def _scroll(browser) -> tuple:
    last_height = browser.execute_script("return document.body.scrollHeight")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    new_height = browser.execute_script("return document.body.scrollHeight")
    return new_height, last_height


# ---------------------------------------------------------------------
def _try_show_more_button(browser) -> bool:
    for wait in range(1, 5 + 1):
        try:
            selector = (
                "div.post-list__show-more-container-f3cf7 > button.kt-button"
            )
            show_more_btn = browser.find_element(By.CSS_SELECTOR, selector)
            show_more_btn.click()
            break
        except NoSuchElementException:
            time.sleep(1)
            if wait == 5:
                return False
    return True


# ---------------------------------------------------------------------
if __name__ == "__main__":
    get_links()
