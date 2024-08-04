"""Spider module to crawl all links"""

import scrapy


class Divar(scrapy.Spider):
    """Read links from urls.csv file and get required data for each."""

    name = "divar_real_estate"
    with open("urls.csv", mode="r", encoding="utf-8", newline="\n") as file:
        start_urls = file.readlines

    def parse(self, response):
        title = response.css(
            "div.kt-page-title__title--responsive-sized::text").extract()
        temp1_info = response.css("p.kt-unexpandable-row__value::text")
        temp2_info = response.css("td.kt-group-row-item--info-row::text")
        description_text = response.css(
            "p.kt-description-row__text--primary::text")
        total_price = temp1_info[0].extract()
        price_per_meter = temp1_info[1].extract()
        which_floor = (
            temp1_info[-1][0].extract()
            if temp1_info[-1][0].extract() != "ه"
            else "0"
        )

        yield {
            "title": title,
            "total_price": total_price,
            "price_per_meter": price_per_meter,
            "which_floor": which_floor,
            "total_floors": temp1_info[-1][-1],
            "meters": temp2_info[0],
            "year_of_construction": temp2_info[1],
            "rooms": temp2_info[2],
            "description_text": description_text[0],
        }
