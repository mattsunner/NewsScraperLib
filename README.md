# NewsScraperLib

## About

NewsScraperLib is a simple Python library created to make scraping news site headlines easier in the data gathering process. The idea arose from the manual process of scraping websites with vastly different structures for text data for sentiment analysis and other NLP applications.

This library is free and open source to use. It is licensed under the MIT license. Once the current version is stable, it will be availalbe on to download through PyPI (pip).

## Licensing

This library is freely distributed under the MIT license. Please see the full license text in the repository.

## Using the Library

The library is built with two main methods at this time. `headlineGather()` & `headlineStorer()`. `headlineGatherer()` is the main method used to scrape websites and return data in the form of a list. This list can then be passed in as one of the arguments to `headlineGatherer()` in order to store the data in a SQLite3 database on the local filesystem.

## Example

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
