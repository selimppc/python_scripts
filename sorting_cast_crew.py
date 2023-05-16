"""
Sorting algorithm
"""
from typing import List, Dict, Any, Tuple

castAndCrew = [
        {
            "artist": {
                "id": "c8149560-f556-4ca8-abbf-a1d9f5d6a634",
                "platformId": "c3c98d1b-c581-452d-a385-941ca69401e9",
                "firstName": "Taskeen",
                "lastName": "Rahman",
                "realName": "Taskeen Rahman",
                "gender": "MALE",
                "bio": "",
                "country": "BD",
                "slug": "taskeen-rahman",
                "images": []
            },
            "roles": [
                "Lead Actor"
            ]
        },
        {
            "artist": {
                "id": "6699eb78-cd2d-4569-86ba-42034e97d246",
                "platformId": "c3c98d1b-c581-452d-a385-941ca69401e9",
                "firstName": "Sunny",
                "lastName": "Sanwar",
                "realName": "Sunny Sanwar",
                "gender": "MALE",
                "bio": "",
                "country": "BD",
                "slug": "sunny-sanwar-27360",
                "images": []
            },
            "roles": [
                "Scriptwriter",
                "Producer",
                "Director"
            ]
        },
        {
            "artist": {
                "id": "215e2abc-13bf-4c27-afc4-c812c2d4ff71",
                "platformId": "c3c98d1b-c581-452d-a385-941ca69401e9",
                "firstName": "Faisal",
                "lastName": "Ahmed",
                "realName": "Faisal Ahmed",
                "gender": "MALE",
                "bio": "",
                "country": "BD",
                "slug": "faisal-ahmed-27379",
                "images": []
            },
            "roles": [
                "Director"
            ]
        },
        {
            "artist": {
                "id": "1bd01d03-fa09-4611-be6d-18d5234b1271",
                "platformId": "c3c98d1b-c581-452d-a385-941ca69401e9",
                "firstName": "Jannatul",
                "lastName": "Ferdous Oishee",
                "realName": "Jannatul Ferdous Oishee",
                "gender": "MALE",
                "bio": "",
                "country": "BD",
                "slug": "jannatul-ferdous-oishee-30712",
                "images": []
            },
            "roles": [
                "Lead Actress"
            ]
        },
        {
            "artist": {
                "id": "1700eb82-97ed-4bea-8af1-6305a94625b3",
                "platformId": "c3c98d1b-c581-452d-a385-941ca69401e9",
                "firstName": "Arifin",
                "lastName": "Shuvoo",
                "realName": "Arifin Shuvoo",
                "gender": "MALE",
                "bio": "",
                "country": "BD",
                "slug": "arifin-shuvoo",
                "images": []
            },
            "roles": [
                "Lead Actor"
            ]
        }
    ]

roles_priority = {
    "Lead Actor": 1,
    "Lead Actress": 2,
    "Director": 3
}

class CrewMember:
    """Artists OR Crew member"""
    def __init__(self, artist: Dict[str, Any], roles: List[str]):
        self.artist = artist
        self.roles = roles

    def as_dict(self) -> Dict[str, Any]:
        return {
            "artist": self.artist,
            "roles": self.roles
        }


class CachedSorting:
    """Caching and Sorting """
    def __init__(self):
        self.cache: Dict[int, List[CrewMember]] = {}

    @staticmethod
    def get_priority(crew_member: CrewMember) -> int:
        """get priority based on role"""
        roles = crew_member.roles
        return min(roles_priority.get(role, float("inf")) for role in roles)

    def sort(self, cast_and_crew: Tuple[CrewMember]) -> List[CrewMember]:
        """sort and cache"""
        cache_key = hash(cast_and_crew)
        if cache_key in self.cache:
            return self.cache[cache_key]

        sorted_data = sorted(cast_and_crew, key=self.get_priority)
        self.cache[cache_key] = sorted_data
        return sorted_data

def display(sorted_cast_and_crew: List[CrewMember], response_array: List[Dict[str, Any]]) -> None:
    """response"""
    for person in sorted_cast_and_crew:
        response_array.append(person.as_dict())


def main() -> None:
    """main"""
    # Convert the list to an immutable tuple
    data_tuple = tuple(CrewMember(**person) for person in castAndCrew)
    sorted_data = CachedSorting().sort(data_tuple)

    response_array = []
    display(sorted_data, response_array)

    print(response_array)


if __name__ == "__main__":
    main()




