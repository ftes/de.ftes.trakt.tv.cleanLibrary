Cleaning your trakt.tv library
==============================

Clean the trakt.tv library by removing all movies and shows


Instructions
------------

Before calling the script, create a trakt-auth.json in the same directory with the following content:
```
{
	"apiKey":	"<trakt-api-key>",
	"user":		"<trakt-username>",
	"pwdSha1":	"<trakt-password-hash (php: sha1('password'))>"
}
```
