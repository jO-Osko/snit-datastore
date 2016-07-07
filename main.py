#!/usr/bin/env python

import os

import jinja2
import webapp2

from models import Sporocilo  # vkljucimo sporocilo

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class IndexHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")


class RezultatHandler(BaseHandler):
    def post(self):

        # Kot prej preberemo besedilo, ki ga je uporabnik vpisal
        besedilo_sporocila = self.request.get("vnos")

        # Naredimo nov objek sporocilo in mu za besedilo nastavimo vpisano besedilo
        sporocilo = Sporocilo(besedilo=besedilo_sporocila)
        # Ker je Sporocilo podedovalo stvari od ndb.Model, je podedovalo tudi konstruktor

        # Shranimo sporocilo v bazo (Spet to metodo dobimo "zastonj" skozi dedovanje)
        sporocilo.put()

        return self.write("Vpisal si: " + sporocilo.besedilo)


class SeznamSporocilHandler(BaseHandler):
    def get(self):
        params = dict()  # Dodatne informacije, ki jih bomo posredovali jinji
        # Iz baze pridobimo vsa sporocila
        vsa_sporocila = Sporocilo.query().fetch()
        params["vsa_sporocila"] = vsa_sporocila
        return self.render_template("seznam_sporocil.html", params=params)

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/rezultat', RezultatHandler),
    ('/seznam-sporocil', SeznamSporocilHandler)
], debug=True)
