#Name: Quy Nguyen
# Consulted Breadth First Search from the following Source: 
# https://github.com/prathameshtajane/spider-web-crawler/blob/master/crawler.py

import socket
import ssl
from bs4 import BeautifulSoup, SoupStrainer


def bfs():

	visited = []
	queue = [{'url': "https://www.rit.edu/", 'depth': 0}]
	urls = []

	while (len(queue)!=0):
		node = queue.pop(0)
		if node['url'] not in (obj['url'] for obj in visited):
			visited.append(node)
			if (node['depth'] < 4):

				urls = processURL(node)
				if len(urls)!=0:
					queue = queue + urls

	return



# return urls to crawl and process emails on page
def processURL(node):


	output = []



	if "https" in node ['url']:
		url = node['url'][19:]

	else:
		url = node['url'][18:]



	hostname = 'www.rit.edu'
	context = ssl.create_default_context()

	with socket.create_connection((hostname, 443)) as sock:
		with context.wrap_socket(sock, server_hostname=hostname) as ssock:
		    request = "GET " + url + " HTTP/1.1\r\nHost: www.rit.edu\r\nAccept: */*\r\n\r\n"
		    ssock.send(request.encode())

		    data=b''
		    while True:
	        	temp=ssock.recv(1)
	        	if temp is None or len(temp)==0:
	        		break
	        	data+=temp

	ssock.close()


	only_a_tags = SoupStrainer("a")
	soup = BeautifulSoup(data, "html.parser", parse_only=only_a_tags)


	#Getting urls
	for link in soup.find_all('a', href=True):
		if "www.rit.edu" in link['href']:
			output.append({'url': link['href'], 'depth': node['depth'] + 1})

	#Getting emails

	for a in soup.select("a[href^=mailto:]"):
		# emails.append({'email': a['href'], 'depth': node['depth'] + 1})


		if "@" not in a['href']:
			continue

		elif node['depth'] == 1:
			file = open("depth1.txt", "a")
			file.write(a['href'][7:])
			file.write("\n")
			file.close()

		elif node['depth'] == 2:
			file = open("depth2.txt", "a")
			file.write(a['href'][7:])
			file.write("\n")
			file.close()

		elif node['depth'] == 3:
			file = open("depth3.txt", "a")
			file.write(a['href'][7:])
			file.write("\n")
			file.close()

		elif node['depth'] == 4:
			file = open("depth4.txt", "a")
			file.write(a['href'][7:])
			file.write("\n")
			file.close()

	return output








def main():


	bfs()

	return



main()