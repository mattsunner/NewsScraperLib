# NewsScraperLib

## About

NewsScraperLib is a simple Python library created to make scraping news site headlines easier in the data gathering process. The idea arose from the manual process of scraping websites with vastly different structures for text data for sentiment analysis and other NLP applications.

This library is free and open source to use. It is licensed under the MIT license. Once the current version is stable, it will be availalbe on to download through PyPI (pip).

## Licensing

This library is freely distributed under the MIT license. Please see the full license text in the repository.

## Using the Library

To use the library in it's current unstable form, follow the steps below:

1. Clone the repo to your local machine
2. Install the library to your local `PATH` using pip
3. Import the package `app` to your project & use as normal (Stable release will contain a full package name)

Full library method documentation can be found [here](./API_Documentation.md)

## Example

Below is sample code that would scrape the Reuters website, pull all headlines with the CSS selector 'h3' as well as a class name of 'story-title'. HeadlineStorer would then store these headlines in an existing SQLite database, or would create one if one did not exist.

```
from application import headlineGatherer, headlineStorer

def main():
    headlines = headlineGatherer('https://reuters.com', 'h3', 'story-title')

    headlineStorer('headlineData.db', headlines)


if __name__ == '__main__':
    main()
```

## Contact & Questions

If you have any questions or suggestions, please feel free to reach out at matt@mattsunner.com.
