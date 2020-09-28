"""
Reuters-Pipeline 
"""

__version__ = '0.1.0'

from application import headlineGatherer


def main():
    headlineGatherer('https://www.reuters.com/', 'h2')


if __name__ == '__main__':
    main()
