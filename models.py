from google.appengine.ext import ndb


# Ustvarimo osnovni model za Sporocilo
class Sporocilo(ndb.Model):
    besedilo = ndb.StringProperty()  # Za zacetek mu dajmo zgolj eno vrednost -> besedilo tega sporocila

