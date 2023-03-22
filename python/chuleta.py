# ID
# results = soup.find(id="ResultsContainer")
# print(results.prettify())

# classname
# job_elements = results.find_all("div", class_="card-content")
# for job_element in job_elements:
#    print(job_element, end="\n"*2)

# text html
# title_element.text
# title_element.text.strip()

# by Class Name and Text Content
# python_jobs = results.find_all("h2", string="Python")

# parent
# h2_element.parent

# findAll
# links = job_element.find_all("a")

# attribute
# link_url = link["href"]

# json
# d = {}
# d['Machine Name'] = hostname
# json.dumps(d)