from google.appengine.ext import ndb


# Ustvarimo osnovni model za Sporocilo
# Sporocilo avtomatsko dobi tudi id() metodo, ki je zelo uporabna za dolocanje
class Sporocilo(ndb.Model):
    besedilo = ndb.StringProperty()  # Za zacetek mu dajmo zgolj eno vrednost -> besedilo tega sporocila
    nastanek = ndb.DateTimeProperty(auto_now_add=True)  # Shranimo si nastanek (to naredimo kar avtomatsko)


#mozne razsiritve
class Email(ndb.Model):
    zadeva = ndb.StringProperty()
    posiljatelj = ndb.StringProperty()
    sporocilo = ndb.TextProperty()  # za daljse besedilo
    poslano = ndb.DateTimeProperty(auto_now_add=True)

    pomembno = ndb.BooleanProperty()
    prebrano = ndb.BooleanProperty()

    stevilo_prejemnikov = ndb.IntegerProperty()
