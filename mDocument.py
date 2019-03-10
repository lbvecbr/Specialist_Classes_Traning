
'Factory Functions'

def create():
    """Create new document"""
    return Document(status=Document.New)

def load(id):
    """Load document from Database"""
    Doc = Document(id=id)
    Doc.restore()
    return Doc

class Document(object):
    """This is persistend object. It should have methods
       save and restore at least"""
    New = 1
    Status_Allowed = [New]
    def __init__(self, **kwargs):
        if 'id' in kwargs:
            self.__Id = int(kwargs['id'])
        if 'status' in  kwargs:
            if kwargs['status'] not in Document.Status_Allowed:
                raise ValueError
            self.__Status = kwargs['status']

    id = property(lambda self: self.__Id)

    @property
    def _id(self):
        try:
            return self.id
        except AttributeError:
            return None

    """ This is the same 
    def getId(self):
        return self.__Id
    id =property(getId)
    """
    @property
    def status(self):
        return self.__Status

    @property
    def _status(self):
        try:
            return self.status
        except AttributeError:
            return None 

    def save(self):
        pass

    def restore(self):
        pass   

if __name__ == '__main__':
    D = create()
    D = load(id=1)
    try:
        print('Status = ', D.status)
    except AttributeError:
        print('<NONE>')
    try:
        print('ID     =',  D.id)
    except AttributeError:
        print('<NONE>')

    D = load(id = '123')
    try:
        print('Status = ', D.status)
    except AttributeError:
        print('<NONE>')
    try:
        print('ID     =',  D.id)
    except AttributeError:
        print('<NONE>')
