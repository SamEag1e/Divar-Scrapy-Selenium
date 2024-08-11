# Scraping_Real_Estate_Divar_Scrapy_Selenium
## Description
Scraping ads from Divar using Scrapy and Selenium
## Features
* **Scraping Ads**: Extract ads from Divar using Scrapy and Selenium.
## Installation
1. Clone the repository:
```
git clone https://github.com/SamEag1e/Scraping_Real_Estate_Divar_Scrapy_Selenium.git
```
2. Navigate to the project directory:
```
cd Scraping_Real_Estate_Divar_Scrapy_Selenium
```
3. Create a virtual environment:
```
python -m venv env
```
4. Activate the virtual environment:
  * On Windows: ```.\env\Scripts\activate```
  * On macOS and Linux: ```source env/bin/activate```
5. Install the required dependencies:
```
pip install scrapy
```
```
pip install selenium
```
## Usage
Run the scraper using:
```
python main.py
```
## To Do
 1. Fix the problem getting blocked with scrapy(add proxy and delay time).
 2. Write to mysql database(using scrapy pipelines?).
 3. Update links.py to get the correct element for ads links.
## Contributing
* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Commit your changes (git commit -m 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.
## License
This project is licensed under the MIT License.
