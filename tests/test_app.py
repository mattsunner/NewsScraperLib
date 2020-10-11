from application import headlineGatherer


def test_headline_gatherer():
    url = 'https://reuters.com'
    tag = 'h3'
    className = 'story-content'

    assert headlineGatherer(url, tag, className) == True
