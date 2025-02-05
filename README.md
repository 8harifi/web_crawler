
# Web Crawler

This is a simple and fast web crawler that extracts URLs and saves the content of web pages. It allows you to crawl a website, collect URLs, and optionally save the content of each page. The script is designed for easy use, with a range of configuration options.

## Features:
- Crawls a single or multiple URLs.
- Allows saving only URLs or full content of each page.
- Supports custom timeouts for requests.
- Configurable to handle a single domain or multiple domains during crawling.
- Outputs data to a file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/web-crawler.git
   ```

2. Navigate to the project directory:
   ```bash
   cd web-crawler/
   ```

3. Install dependencies:
   ```bash
   pip install requests beautifulsoup4 termcolor
   ```

4. Run the script:
   ```bash
   python crawler.py [options] <url>
   ```

## Usage

### Options:

- `--single-domain`  
  Crawl only URLs that belong to the same domain as the main URL.

- `--output`, `-o`  
  Specify the output file name. Default is `output.txt`.

- `--time-out`, `-t`  
  Set a custom timeout (in seconds) for the requests.

- `--contents`  
  Save the contents of each page.

- `--urls`  
  Save only the URLs found on the crawled pages.

### Example:

```bash
python crawler.py --single-domain --output my_output.txt --time-out 10 --contents https://example.com
```

### Default Configuration:
If no options are specified, the script will:
- Save only URLs.
- Crawl all URLs within the same domain.
- Output to `output.txt`.

## Script Behavior

- **Crawling:** The script starts by crawling the specified URL and searches for all links (`<a href>` tags).
- **URL extraction:** Extracts and follows any URLs within the same domain, and optionally external URLs, based on the specified options.
- **Output:** It saves the URLs or the entire HTML content of the crawled pages to the output file.

## Example Output:

When saving URLs:
```
https://example.com/page1: 200
https://example.com/page2: 404
https://example.com/page3: 200
...
```

When saving content:
```
<html>
<head><title>Example Page</title></head>
<body>Content here...</body>
</html>

---------------------------------------------------------------------------

<html>
<head><title>Another Page</title></head>
<body>Another content here...</body>
</html>
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
