# <img src="https://img.shields.io/badge/Status-Completed-green" alt="Status"> Crawler

[![GitHub license](https://img.shields.io/github/license/bizkwit/Crawler)](https://github.com/bizkwit/Crawler/blob/main/LICENSE)



## Overview

This project implements a multi-threaded web crawler designed to efficiently explore websites and extract links within a given domain.  The crawler utilizes multiple threads to concurrently fetch and process web pages, significantly speeding up the crawling process.  It maintains lists of URLs to visit and URLs already visited to prevent redundant crawling and ensure efficient resource utilization.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
- [Examples](#examples)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)


## Features

* **Multi-threaded crawling:**  Utilizes multiple threads for concurrent page fetching and processing, leading to faster crawling.
* **Efficient URL management:** Maintains separate lists of URLs to visit and URLs already visited to avoid redundancy.
* **Domain restriction:** Crawls only links within the specified domain, preventing the crawler from straying outside the target website.
* **Error handling:** Includes error handling mechanisms to gracefully handle issues like network problems or invalid URLs.
* **Data persistence:** Stores visited and unvisited URLs in files for resuming crawls later.


## Technologies

* [Python](https://www.python.org/) <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Beautiful_Soup_logo.svg/1200px-Beautiful_Soup_logo.svg.png" alt="Beautiful Soup" width="40" height="40"/>
* [urllib](https://docs.python.org/3/library/urllib.html)
* [threading](https://docs.python.org/3/library/threading.html)


## Getting Started

### Prerequisites

* Python 3.x installed on your system.
* Required Python packages: `beautifulsoup4`, `urllib3`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bizkwit/Crawler.git
   cd Crawler
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt 
   ```

### Usage

1. Run the `main.py` script.
2. Enter the project name and the base URL of the website you want to crawl when prompted.

The crawler will create a directory for the project, containing files to store visited and unvisited URLs.  The crawling process will continue until all URLs in the queue have been processed.


## Examples

To crawl `example.com`, run the script and provide the following input:

* **Project Name:**  `example_crawl`
* **Homepage:** `https://www.example.com`


## Roadmap

- [x] Implement basic web crawling functionality.
- [x] Add multi-threading for improved performance.
- [x] Implement URL management (visited and unvisited lists).
- [x] Add domain restriction to prevent crawling unrelated sites.
- [x] Improve error handling.
- [x] Add data persistence (saving and loading URL lists).
- [ ] Implement a more robust error handling system (e.g., retry mechanisms).
- [ ] Add support for robots.txt.
- [ ] Add options for configuring crawl depth and politeness parameters.
- [ ] Add data output options (e.g., saving extracted data to a database or CSV file).



## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgements

* This project was inspired by [mention any inspirations or resources].
