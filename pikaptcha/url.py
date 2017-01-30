import urllib.request, urllib.error, urllib.parse

def openurl(address):
    try:
        urlresponse = urllib.request.urlopen(address).read()
        return urlresponse        
    except urllib.error.HTTPError as e:
        print(("HTTPError = " + str(e.code)))
    except urllib.error.URLError as e:
        print(("URLError = " + str(e.code)))
    except Exception:
        import traceback
        print(("Generic Exception: " + traceback.format_exc()))
    print(("Request to " + address + "failed."))
    return "Failed"

def activateurl(address):
    try:
        urlresponse = urllib.request.urlopen(address)
        return urlresponse
    except urllib.error.HTTPError as e:
        print(("HTTPError = " + str(e.code)))
    except urllib.error.URLError as e:
        print(("URLError = " + str(e.code)))
    except Exception:
        import traceback
        print(("Generic Exception: " + traceback.format_exc()))
    print(("Request to " + address + "failed."))
    return "Failed"