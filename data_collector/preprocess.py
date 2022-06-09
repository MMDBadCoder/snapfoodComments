# import required module
import json
import os

directory = 'comments/'

comments_by_rate = {}
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = '\n'.join(file.readlines())
            comments = json.loads(content)
            for comment in comments:
                commentText = comment['commentText']
                rate = comment['rate']
                if not comments_by_rate.__contains__(rate):
                    comments_by_rate[rate] = []
                comments_by_rate[rate].append(commentText)

for rate, comments in comments_by_rate.items():
    with open('comments_by_rate/' + str(rate) + '.csv', 'w') as file:
        file.writelines([comment for comment in comments if comment is not None])
        file.flush()
