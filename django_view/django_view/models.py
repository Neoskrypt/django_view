from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth = models.DateField()

    def to_dict(self):
        return {'name': self.name,
                'surname': self.surname,
                'birth': str(self.birth)}

    @staticmethod
    def from_dict(dct: dict):
        return Artist(name=dct.get('name'),
                      surname=dct.get('surname'),
                      birth=dct.get('birth'))
