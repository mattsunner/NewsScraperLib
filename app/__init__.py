"""
Reuters-Pipeline 
"""

__version__ = '0.1.0'

from application import headlineGatherer


def main():
    x = headlineGatherer('https://www.reuters.com/', 'h3')
    print(x)


if __name__ == '__main__':
    main()
