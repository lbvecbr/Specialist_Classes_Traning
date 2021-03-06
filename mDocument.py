import sqlite3
import os


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
        # TODO: 1. Запомнить значения остальных параметров,
        # TODO:    но никак их не обрабатывать
        if 'id' in kwargs:
            self.__Id = int(kwargs['id'])
        if 'status' in kwargs:
            if kwargs['status'] not in Document.Status_Allowed:
                raise ValueError
            self.__Status = kwargs['status']

    id = property(lambda self: self.__Id)

    """ This is the same 
    def getId(self):
        return self.__Id
    id =property(getId)
    """

    @property
    def _id(self):
        try:
            return self.id
        except AttributeError:
            return None

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

    @classmethod
    def create_table(self):
         # TODO: 1. Автоматически вычислять SQL-комманду создания таблицы
        conn = sqlite3.connect(os.path.expanduser('~/data.db'))
        curr = conn.cursor()
        curr.execute(
            """
            create table t_document(
            -- TODO: 1. Сделать возможность сохранение в базе
            -- TODO:         дополнительных параметров
            i_id      integer  not null primary key autoincrement,
            f_status  integer  null
            );
            """
        )
        conn.commit()
        conn.close()
        print("Creating documents table")


if __name__ == '__main__':
    Document.create_table()
    D = create()
    D = load(id=1)
    try:
        print('Status = ', D.status)
    except AttributeError:
        print('<NONE>')
    try:
        print('ID     =', D.id)
    except AttributeError:
        print('<NONE>')

    D = load(id='123')
    try:
        print('Status = ', D.status)
    except AttributeError:
        print('<NONE>')
    try:
        print('ID     =', D.id)
    except AttributeError:
        print('<NONE>')
