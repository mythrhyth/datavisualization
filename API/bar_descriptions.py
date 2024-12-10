import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333346', base_style = LCS)

chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legentd = False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = {
    'value': repo_dict['stargazers_count'],
    'label': repo_dict['description'],
    'xlink': repo_dict['html_url']}


plot_dicts.append(plot_dict)
chart.add('', plot_dicts)
chart.render_to_file('Bar_descriptions.svg')