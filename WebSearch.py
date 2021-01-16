#from googlesearch.googlesearch import GoogleSearch
import wikipedia
#Google Searcher
"""def Google (ln):
 resp = GoogleSearch().search(str(ln))
 for result in resp.results:
  return (result.title+"\n"+result.getText())"""
#Wikipedia searcher
def Wiki(ln):
 return wikipedia.summary(str(ln))
