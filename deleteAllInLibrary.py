import json
import requests

# Add a 'trakt-auth.json' in the same directory with the following structure:
# {
# 	"apiKey":	"<trakt-api-key>",
# 	"user":		"<trakt-username>",
# 	"pwdSha1":	"<trakt-password-hash (php: sha1('password'))>"
# }

# Set necessary data
URL_BASE	= "http://api.trakt.tv/"
METHODS		= {"listMovies": "user/library/movies/collection.json/",
			"listShows": "user/library/shows/collection.json/",
			"deleteMovies": "movie/unlibrary/",
			"deleteShow": "show/unlibrary/"}

# Get the authentication data from the json file
traktAuthFile	= open("trakt-auth.json")
traktAuth	= json.load(traktAuthFile)
API_KEY		= traktAuth["apiKey"]
USER		= traktAuth["user"]
PWD_SHA1	= traktAuth["pwdSha1"]

AUTH = {"username": USER, "password": PWD_SHA1}


# for authenticated "GET" methods, trakt.tv actually requires a POST to be issued
# however, the API doc still lists these as GET methods, and their structure is a bit different
def buildGetUrl(method):
	return URL_BASE + method + API_KEY + "/" + USER

def buildPostUrl(method):
	return URL_BASE + method + API_KEY



def deleteMovies():
	r = requests.post(buildGetUrl(METHODS["listMovies"]), data=AUTH)
	movies = r.json()
	movies = {"movies": movies}
	deleteData = dict(AUTH.items() + movies.items())
	r = requests.post(buildPostUrl(METHODS["deleteMovies"]), data=json.dumps(deleteData))

def deleteShows():
	r = requests.post(buildGetUrl(METHODS["listShows"]), data=AUTH)
	shows = r.json()
	for show in shows:
		deleteData = dict(AUTH.items() + show.items())
		r = requests.post(buildPostUrl(METHODS["deleteShow"]), data=json.dumps(deleteData))


if __name__ == "__main__":
	deleteMovies()
	deleteShows()
