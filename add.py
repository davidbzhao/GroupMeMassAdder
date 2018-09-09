import json
import requests
import sys
import unicodedata
import yaml

def get_access_token():
  with open('auth.yml', 'r') as infile:
    auth_obj = yaml.load(infile.read())
    assert 'groupme' in auth_obj, "Token 'groupme' not in auth.yml"
    return auth_obj['groupme']

def get_group_id(name):
  base_url = 'https://api.groupme.com/v3/groups'
  params = {
    'token': get_access_token(),
    'per_page': 500
  }
  response = requests.get(base_url, params=params)
  response_text = response.text
  response_json = json.loads(response_text)

  for group in response_json['response']:
    group_name = unicodedata.normalize('NFKD', group['name'])
    if group_name == name:
      return group['group_id']
  return None
  
def get_members_to_add(infile_path):
  members = []
  with open(infile_path, 'r') as infile:
    lines = infile.readlines()
    for line in lines:
      line_split = line.split(',')
      assert len(line_split) >= 2, 'Name and phone number must be provided'
      name, number = [s.strip() for s in line_split]
      members.append({
        'nickname': name,
        'phone_number': '+1 {}'.format(number)
      })
  return {
    'members': members
  }

def add_members(group_id, members):
  base_url = 'https://api.groupme.com/v3/groups/{}/members/add?token={}'.format(group_id, get_access_token())
  response = requests.post(base_url, json=members)
  print(response)


if __name__ == '__main__':
  group_name = input('Group name? ')
  group_id = get_group_id(group_name)
  assert group_id, 'Group not found'

  infile_path = input('Path to csv of members? ')
  members = get_members_to_add(infile_path)
  add_members(group_id, members)

