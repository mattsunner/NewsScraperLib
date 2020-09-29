"""
Reuters-Pipeline 
"""

__version__ = '0.1.0'

from application import headlineGatherer


def main():
    print(headlineGatherer('https://www.reuters.com/', 'div', 'story-title'))


if __name__ == '__main__':
    main()
