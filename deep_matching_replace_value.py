"""
Deep matching  algorithm
"""
import json
import re
from typing import List, Dict

data_one = {
  "items": [
    {
      "bongoId": "SIfHTF0kpyE",
      "highlight": {
          "title": [
              "<em>Jack</em> 420  | EP <em>Jack</em> 02"
          ],
          "genres": [
              "<em>Jack</em> son",
              "<em>Jack</em> <em>jack</em> action"
          ],
          "artists": [
              "Fahim <em>Jack</em>",
              "A. <em>Jack</em>"
          ],
      },
      "id": "e18cf535-f8c4-4f6a-a547-41e4754bab9a",
      "title": "Comedy 420 | EP Jack 02",
      "type": ""
    }
  ]
}

data_two = {
    "items": [
        {
            "id": "e18cf535-f8c4-4f6a-a547-41e4754bab9a",
            "platformId": "",
            "title": "Comedy 420 | EP Jack 02",
            "contentType": "VOD_SINGLE",
            "systemId": "SIfHTF0kpyE",
            "slug": "comedy-hour-2014-10-05-1",
            "castAndCrew": [
                {
                    "artist": {
                        "firstName": "Fahim",
                        "lastName": "Jack ",
                        "realName": ""
                    },
                    "roles": [
                        "Lead Actor"
                    ]
                },
                {
                    "artist": {
                        "firstName": "A.",
                        "lastName": "Jack ",
                        "realName": "Siddiqur Rahman Siddique"
                    },
                    "roles": [
                        "Lead Actor"
                    ]
                },
                {
                    "artist": {
                        "firstName": "Afjal",
                        "lastName": "Sharif ",
                        "realName": "Afjal Sharif"
                    },
                    "roles": [
                        "Lead Actor"
                    ]
                },
                {
                    "artist": {
                        "firstName": "Harun",
                        "lastName": "Kisingar ",
                        "realName": ""
                    },
                    "roles": [
                        "Lead Actor"
                    ]
                },
                {
                    "artist": {
                        "firstName": "Saed",
                        "lastName": "Tareq",
                        "realName": ""
                    },
                    "roles": [
                        "Director"
                    ]
                }
            ],
            "genre": [
                {
                    "name": "Jack son"
                },
                {
                    "name": "Jack jack action"
                }
            ]
        },

    ]
}

def remove_html_tags(text: str) -> str:
    """
    Remove html tags from a string
    :text string <em> included:
    """
    return re.sub('<.*?>', '', text).strip()


def update_title(source_item: Dict, target_item: Dict) -> None:
    """
    Update title in the target item
    :param source_item:
    :param target_item:
    :return:
    """
    title_list = source_item['highlight'].get('title')
    if title_list:
        target_item['title'] = title_list.pop()


def update_artists(source_item: Dict, target_item: Dict) -> None:
    """
    Update artists in the target item
    :param source_item:
    :param target_item:
    """
    for artist in target_item.get('castAndCrew', []):
        full_name = f"{artist['artist'].get('firstName', '')} " \
                    f"{artist['artist'].get('lastName', '')}".strip()
        for crew_name in source_item['highlight'].get('artists', []):
            if full_name.strip() in remove_html_tags(crew_name):
                first_name, last_name = crew_name.split(' ', 1)
                artist['artist']['firstName'] = first_name
                artist['artist']['lastName'] = last_name


def update_genres(source_item: Dict, target_item: Dict) -> None:
    """
    Update genres in the target item
    :param source_item:
    :param target_item:
    """
    for genre in target_item.get('genre', []):
        for item in source_item['highlight'].get('genres', []):
            if genre['name'].strip() in remove_html_tags(item):
                genre['name'] = item


def update_data(source_data: List[Dict], target_data: List[Dict]) -> List[Dict]:
    """
    update target data by source_data -> highlights
    :param source_data:
    :param target_data:
    :return:
    """
    for i in source_data:
        for j in target_data:
            # Check if the IDs match
            if i.get('bongoId') == j.get('systemId') or \
                    i.get('id') == j.get('id'):
                # update title, artists and genres
                update_title(i, j)
                update_artists(i, j)
                update_genres(i, j)
    return target_data


def main() -> None:
    """main"""

    result = update_data(source_data=data_one['items'], target_data=data_two['items'])
    response = json.dumps(result)
    print(response)


if __name__ == "__main__":
    main()




