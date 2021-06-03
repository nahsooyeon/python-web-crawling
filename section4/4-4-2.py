import simplejson as json

#Dict(Json)선언
data = {}
data['people'] = []
data['people'].append({
    'name': 'Kim',
    'website': 'naver.com',
    'from': 'Seoul',
    'grade': [95,77,89,91]
})
data['people'].append({
    'name': 'Park',
    'website': 'google.com',
    'from': 'Busan',
    'grade': [85,67,100,94]
})
data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon',
    'grade': [98,79,99,92]
})

#data = {'people': [{'name': 'Kim', 'from': 'Seoul', 'website': 'naver.com', 'grade': [95,77,89,91]}, {'name': 'Park', 'from': 'Busan', 'website': 'google.com', 'grade': [85,67,100,94]}, {'name': 'Lee', 'from': 'Incheon', 'website': 'daum.net', 'grade': [98,79,99,92]}]}

#json 파일 쓰기(dump)
with open('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/member.json','w') as outfile:
    json.dump(data, outfile)
#
#json 파일 읽기(load)
with open('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/member.json', 'r') as infile:
    r = json.load(infile)
    # print(type(r))
    # print(r)
    print('===================')

    for p in r['people']:
        print('Name: ' +  p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        t = p['grade'] # 배
        grade = ''
        for g in p['grade']:
            grade = grade + ' ' + str(g)
        print('Grade:', grade.lstrip()) # 왼쪽 공백 제거 오른쪽공백제거: rstrip()
        print('')
