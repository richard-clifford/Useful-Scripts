import requests
import re
import ssl

targets = open("targets.txt", 'r').readlines()

for target in targets:
  target = target.rstrip()

  headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)'}
  
  response = requests.get(target.split('|')[0], headers=headers).text  

  scanjs = re.findall(r'src="([^"]+\.js|json)?"',response) 

  for i in scanjs:

    new_target = target + i

    if(re.match(r'(http|https)\:\/\/',i)):
      new_target = i

    js_file_request = requests.get(new_target, headers=headers).text
    callback_possibru = re.findall(r'(callback|jsonp)', js_file_request)

    for x in callback_possibru:
      print " --- VULN --- \n"
      print "["+target+"] " + new_target + " " + x  