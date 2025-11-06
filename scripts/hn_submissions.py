from operator import itemgetter
import requests
from typing import TypedDict, List
import plotly.express as px

class Story(TypedDict):
    by: str
    descendants: int
    id: int
    title: str
    hn_link: str
    type: str

# Make an API call and check the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    if(r.status_code == 200):
        response_dict = r.json()
        try:
            news_id = response_dict["id"]
            comments = response_dict["descendants"]
        except KeyError:
            print(f"Skipping id: {news_id}. Coudn't find 'descendants'.")
        else:
            # Build a dictionary for each article.
            submission_dict: Story = {
                "by": response_dict["by"],
                "descendants": comments,
                "id": news_id,
                "title": response_dict["title"],
                "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
                "type": response_dict["type"],
            }
            submission_dicts.append(submission_dict)
    else:
        print(f"Something Happened. Status Code: {r.status_code}")

submission_dicts = sorted(submission_dicts, key=itemgetter("descendants"), reverse=True)

news_links, total_comments, hover_texts = [], [], []

for submission_dict in submission_dicts:
    # Make clickable links (x)
    news_title = submission_dict["title"]
    repo_url = submission_dict["hn_link"]
    link = f"<a href='{repo_url}' style='color:black; text-decoration:none;'>{news_title}</a>"

    # Captures number of comments for specific news_discus (y)
    comments = submission_dict["descendants"]

    # build hover texts
    op = submission_dict["by"]
    type_story = submission_dict["type"]
    hover_text = f"Posted by: {op}<br />(type): {type_story}"

    # Appending
    news_links.append(link)
    total_comments.append(comments)
    hover_texts.append(hover_text)

# Make visualization.
title = "Hacker News"
labels = {"x": "Post Title", "y": "Comments"}
fig = px.bar(
    x=news_links, y=total_comments, title=title, labels=labels, hover_name=hover_texts,
)

fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    yaxis=dict(
        tickfont=dict(color="black"),  # makes x labels black
        # tickangle=-45,  # keeps them angled (optional)
    ),
)

fig.update_traces(marker_color="gold", marker_opacity=0.8)

fig.show()

"""
Example 45816853
{
    "by": "speckx",
    "descendants": 76,
    "id": 45816853,
    "kids": [45817800, 45817789, 45817405, 45818311, 45819990, 45819885, 45817950, 45817389, 45818628, 45817960, 45819918, 45818630, 45818314, 45817775, 45818500, 45817844, 45817707, 45818078, 45818356, 45817310, 45817575, 45817993, 45819683, 45819685, 45820594, 45818886, 45819921],
    "score": 587,
    "time": 1762297032,
    "title": "Mr TIFF",
    "type": "story",
    "url": "https://inventingthefuture.ghost.io/mr-tiff/"
}
"""
