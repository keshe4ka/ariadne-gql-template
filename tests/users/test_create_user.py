import json


def test_create_user(test_app, test_db):
    query = """
        mutation ($input: UserInput!){
            createUser(data: $input) {
                user {
                    id
                    name
                    email
                }
                error {
                    code
                    message
                }
            }
        }
        """

    variables = {
        'input': {
            'name': 'Test User',
            'email': 'test@mail.ru'
        }
    }

    response = test_app.post(
        url='/',
        json={'query': query, 'variables': variables}
    )

    user = response.json()['data']
    print(response.json())
    assert user['name'] == variables['input']['name']
