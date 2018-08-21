from cgi import parse_qs

def app(env,start_response):
 status='200 OK'
 headers=[
  ('Content-Type','text/plain')
 ]
 body=[env['QUERY_STRING'].replace('&', '\n\'')]
 start_response(status,headers)
 return body
