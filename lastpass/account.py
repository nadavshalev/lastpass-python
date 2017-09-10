# coding: utf-8
class Account(object):
    def __init__(self, id, name, username, password, url, group, notes):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.url = url
        self.group = group
        self.notes = notes
    def __str__(self):
        return "name: {}\n\tusername: {}\n\tpassword: {}\n\turl: {}\n\tgroup: {}\n\tnotes: {}\n\n".format(self.name, self.username, self.password, self.url, self.group, self.notes)
class SecureNote(object):
    def __init__(self):
        pass
    def __str__(self):
        res = ''
        for a in dir(obj):
            res = a.name + '\n\t'
            if not a.startswith('__'):
                res += a + ": " + getattr(self, a) + "\n\t"
        return res + '\n\n'
