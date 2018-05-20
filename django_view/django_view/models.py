from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth = models.DateField()

    def to_dict(self):
        return {'name': self.name,
                'surname': self.surname,
                'birth': str(self.birth),
                "id":str(self.id)}

    @staticmethod
    def from_dict(dct: dict):
        return Artist(name=dct.get('name'),
                      surname=dct.get('surname'),
                      birth=dct.get('birth'))

class Song(models.Model):
    name = models.CharField(max_length=150)
    date_released = models.DateField()
    author = models.ForeignKey(Artist,on_delete="")

    def to_dict(self):
        return {
                'name':self.name,
                'date_released':self.date_released,
                'author':self.author.to_dict()
        }
    @staticmethod
    def from_dict(dct:dict):
        return Song(name=dct.get('name'),
                    date_released = dct.get('date_released'),
                    author = dct.get('author')
        )
