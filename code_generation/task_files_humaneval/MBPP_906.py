# MBPP/906
### Completion
import re

def extract_date(url):
    """
    Extracts the year, month, and date from a given URL using regex.

    Args:
    url (str): The URL from which to extract the date.

    Returns:
    list: A list of tuples containing the year, month, and date.
    """
    # Regex pattern to match the date in the format YYYY/MM/DD
    pattern = r'(\d{4})/(\d{2})/(\d{2})'
    
    # Search for the pattern in the URL
    matches = re.findall(pattern, url)
    
    # Return the matches as a list of tuples
    return [tuple(match) for match in matches]

# Test case
assert extract_date("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/") == [('2016', '09', '02')]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_date("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/") == [('2016', '09', '02')]
    assert extract_date("https://www.indiatoday.in/movies/celebrities/story/wp/2020/11/03/odeof-sushant-singh-rajput-s-death-his-brother-in-law-shares-advice-for-fans-1749646/") == [('2020', '11', '03')]
    assert extract_date("https://economictimes.indiatimes.com/news/economy/2020/12/29/finance/pension-assets-under-pfrda-touch-rs-5-32-lakh-crore/articleshow/79736619.cms") == [('2020', '12', '29')]
