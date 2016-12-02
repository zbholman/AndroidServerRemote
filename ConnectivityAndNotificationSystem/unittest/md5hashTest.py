
import hashlib
import md5

def md5hash():
        m = md5.new()
        m.update('{"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}')
        dstring = m.hexdigest()
        print(dstring)
        if(dstring == "cc0b8a0fd9829ba4de011501058bb4ba"):
                return True

md5hash()
