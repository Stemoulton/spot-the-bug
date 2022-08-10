from argparse import ArgumentParser
from typing import List, Dict
import requests
import json

MAX_PER_REQUEST = 10

class APIError(Exception):
    def __init__(self, *args, response, **kwargs):
        super().__init__(*args, **kwargs)
        self.response = response


def get_animals(num_animals: int) -> List[Dict[str, str]]:
    """
    Request a number of animal objects from the Zoo animal API
    Args:
        num_animals: the number of animal objects to retrieve. Maximum number of animals is
            capped by the API at `MAX_PER_REQUEST`
    returns: list of animals objects
    """
    resp = requests.get(f"https://zoo-animal-api.herokuapp.com/animals/rand/{num_animals}")
    try:
        output = json.loads(resp.text)
    except json.JSONDecodeError:
        raise APIError(response=resp.text)
    return output


def page_animals(num_animals: int):
    """
    Page over requests for animal objects to allow retrieval of > `MAX_PER_REQUEST`
    animal objects
    Args:
        num_animals: the number of animal objects to retrieve
    returns: yields batches of animals from the requests made to the API
    """
    total_requests, remainder = divmod(num_animals, MAX_PER_REQUEST)
    for _ in range(total_requests):
        return get_animals(MAX_PER_REQUEST)
    yield get_animals(remainder)


if "__name__" == __main__:
    parser = ArgumentParser(description="Retrieve random animals and their diets")
    parser.add_argument("-n", "--num-animals", default=10, type=int)
    args = parser.parse_args()

    descriptions = []
    try:
        for animals in page_animals(args.num_animals):
            descriptions.append([f"{d['name']} - {d['diet']}" for d in animals])
    except APIError as e:
        print(f"API Error: {e}")
    else:
        print("\n".join(descriptions))
