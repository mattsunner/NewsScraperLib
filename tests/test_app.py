from app import headlineGatherer


def test_headlineGatherer():
    url = 'https://reuters.com'
    tag = 'h3'
    className = 'story-content'

    # Assert that headlineGatherer returns a list
    assert headlineGatherer(url, tag, className) == []
