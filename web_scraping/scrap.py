from bs4 import BeautifulSoup
import requests

def scrap_index_html():
    with open('index.html', 'r') as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content, 'lxml')
        tag = soup.find('h5') # find only one h5 tags
        print(tag)

        courses_html_tags = soup.find_all('h5') 
        for course in courses_html_tags:
            print(course.text)
        
        course_cards = soup.find_all('div', class_='card')
        for course in course_cards:
            course_name = course.h5.text
            course_price = course.a.text.split()[-1]
            print(f'{course_name} costs {course_price}')

def scrap_from_url():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation='
    html_text = requests.get(url).text  
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            # write csv file
            with open('jobs.csv', 'a') as f:
                f.write(f"{company_name.strip()}, {skills.strip().replace(',',' ')}, {more_info}\n")

            print(f"Company Name: {company_name.strip()}")
            print(f"Required Skills: {skills.strip()}")
            print(f"More Info: {more_info}")
            print('') 

scrap_from_url()