import requests
import json
import collections

import_site = requests.get("https://jsonplaceholder.typicode.com/posts")


try:
    decoded_posts = import_site.json()

except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    most_posts = []
    for line in decoded_posts:
        most_posts.append(line["userId"])
    print(most_posts)

    final_count = collections.Counter(most_posts)
    print(final_count)