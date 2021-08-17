import requests, json, csv

from scrape_config import N, COURSE_NAME, cookies_data, header_data

URL = "https://hello.iitk.ac.in/api/eso204a21/lectures/summary"

mook_response = requests.get(URL,cookies=cookies_data,headers=header_data)
if mook_response.status_code == 200:
    print("Sucesfully authenticated")
else :
    print('----------------------------------------------')
    print(f"Authentication failed, Please verify that you've entered the correct cookies, and header values ")
    exit()
mook_json = json.loads(mook_response.text)


x = len(mook_json)-1
tmp = N

csv_file_header = ['Lecture Name','Week', 'Link']

with open('lecture_results.csv','w',encoding="UTF8") as f:
    helper = csv.writer(f)
    helper.writerow(csv_file_header)
    while not x<0:
        if tmp<=0:
            break
        f = mook_json[x]
        video_links_arr = f['videosUploaded']
        for xx in video_links_arr:
            if xx['type']=='original':
                row_add = [f['topic'] , f['week'] , xx['path'] ]
                helper.writerow(row_add)
        tmp-=1
        x-=1
    
print("Done scraping, Stored the results at \'./lecture_results.csv\'")
