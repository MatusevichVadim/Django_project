import requests

username: str = ''
password: str = ''
base_url: str = 'http://127.0.0.1:8000/api/'

r = requests.get(f'{base_url}courses/', timeout=30)
# print(r.status_code)
courses = r.json()

available_courses: str = ', '.join([course['title'] for course in courses])
print(f'Available courses: {available_courses}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(f'{base_url}courses/{course_id}/enroll/',
                      auth=(username, password),
                      timeout=30)
    if r.status_code == 200:
        print(f'Successfully enrolled in {course_title}')
