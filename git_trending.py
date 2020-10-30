from datetime import datetime
from datetime import timedelta
import requests


def get_trending_repositories(quantity):
    last_week = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    search_params = {
        'q': 'created:>={}'.format(last_week),
        'sort': 'stars',
        'order': 'desc'
    }
    url = 'https://api.github.com/search/repositories'
    trending_repos = requests.get(
        url,
        params=search_params
    ).json()['items'][:quantity]
    return trending_repos


def get_issue_amount(repository):
    url = 'https://api.github.com/repos/{}/issues'.format(
        repository['full_name']
    )
    return len(requests.get(url).json())


if __name__ == '__main__':
    trending_repos_quantity = 20
    trending_repositories = get_trending_repositories(trending_repos_quantity)
    delimiter = '-' * 80
    for repo in trending_repositories:
        print('Repo Owner: \t\t{}'.format(repo['owner']['login']))
        print('Repo Name: \t\t{}'.format(repo['name']))
        print('Open Issues Amount: \t{}'.format(get_issue_amount(repo)))
        print('Repo Link: \t\t{}'.format(repo['html_url']))
        print(delimiter)