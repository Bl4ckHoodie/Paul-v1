try:
  from googlesearch import search 
  import webbrowser
except ImportError:  
  print("No module named 'google' found")#if not found then do pip install google
def get_search():
	query = input('Google search: ')
	return query

def google_get_link(query):
	for i in search(query, tld="co.in", num=10, stop=1, pause=2): 
		return i
def google_search(query):
   if query == '':
        query = get_search()
        link = google_get_link(query)
   else:
        link = google_get_link(query)
   webbrowser.open(link,1)
   return "Link has been successfully openned"
	
