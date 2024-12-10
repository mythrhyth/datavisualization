import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'


r = requests.get(url)
print('Status Code:', r.status_code)


if r.status_code == 200:
    submission_ids = r.json()
    submission_dicts = []

    
    for submission_id in submission_ids[:30]:
        url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
        submission_r = requests.get(url)
        print('Story Status Code:', submission_r.status_code)

        if submission_r.status_code == 200:
            response_dict = submission_r.json()

            submission_dict = {
                'title': response_dict.get('title', 'No title'),
                'link': f'http://news.ycombinator.com/item?id={submission_id}',
                'comments': response_dict.get('descendants', 0)
            }
            submission_dicts.append(submission_dict)

    # Sort the submissions by the number of comments
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

    # Display the sorted submissions
    for submission_dict in submission_dicts:
        print('\nTitle:', submission_dict['title'])
        print('Discussion Link:', submission_dict['link'])
        print('Comments:', submission_dict['comments'])
        
    my_style = LS('#333366', base_style = LCS)
    chart = pygal.Bar(style = my_style,  width = 1000, height = 600, x_label_rotation = 45, truncate_label = 20, show_legend = False)
    
    chart.title = 'Submissions and Discussions'
    titles = [submission['title'] for submission in submission_dicts]
    comments = [submission['comments'] for submission in submission_dicts]
    chart.xlabels = titles
    chart.add('Comments', comments)
    chart.render_to_file('hacker_news_submissions.svg')
    
else:
    print("Failed to fetch data from Hacker News API.")
