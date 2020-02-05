from pyramid.request import Request
from pyramid.view import view_config


def get_test_shows():
    return [
        {'day': 'Monday 02-03', 'location': '', 'time': '', 'title': '', 'url': '', 'description': ''},
        {'type': 'film', 'day': '', 'location': 'City 46', 'time': '17:30', 'title': 'Romys Salon', 'url': 'http://www.city46.de/programm/februar-2020/demenz.html#c37522', 'description': 'NL/D 2018, ab 8 Jahren'},
        {'type': 'film', 'day': '', 'location': 'City 46', 'time': '18:00', 'title': 'Our Struggles – Nos Batailles', 'url': 'http://www.city46.de/programm/februar-2020/thema-des-monats-cinema-mon-amour.html#c37534', 'description': 'B/F 2018 Im Lager eines großen Händlers kämpft Olivier mit vollem Einsatz als Gewerkschafter für den Arbeitsplatz eines 53-jährigen Mitarbeiters.'},
        {'type': 'music', 'day': '', 'location': 'Glocke', 'time': '18:30', 'title': 'Schubert - sonatas', 'url': 'http://www.city46.de/programm/februar-2020/thema-des-monats-cinema-mon-amour.html#c37534', 'description': '30€ and it is nice music'},
        {'type': 'film', 'day': '', 'location': 'Schauburg', 'time': '19:00', 'title': 'Sorry we missed you', 'url': 'http://www.bremerfilmkunsttheater.de/Kino_Reservierungen/Schauburg.html', 'description': 'Abby und ihre zwei Kinder leben in Newcastle. Sie sind eine starke, liebevolle Familie, in der jeder für den anderen einsteht. Während Ricky sich mit Gelegenheitsjobs durchschlägt (...)'},
        {'type': 'film', 'day': '', 'location': 'City 46', 'time': '20:30', 'title': 'Darkroom – Tödliche Tropfen', 'url': '', 'description': ''},
        {'type': 'film', 'day': '', 'location': 'Schauburg', 'time': '21:00', 'title': 'Jojo Rabbit', 'url': 'http://www.bremerfilmkunsttheater.de/Kino_Reservierungen/Schauburg.html', 'description': ''},
        {'day': 'Tuesday 02-04', 'location': '', 'time': '', 'title': '', 'url': '', 'description': ''},
        {'type': 'stage', 'day': '', 'location': 'Schwankhalle', 'time': '09:00', 'title': 'Ein Filmprojekt im Theater', 'url': 'https://schwankhalle.de/spielplan/schnupperworkshop-die-erde-ist-rund-756.html', 'description': 'Schnupperworkshop für Kinder zwischen 9 und 12 Jahren'},
        {'type': 'film', 'day': '', 'location': 'Glocke', 'time': '09:00', 'title': 'GLOCKE Spielraum - Winterferien: - »Bühnenreif!«', 'url': 'https://www.glocke.de//de/Veranstaltungssuche/04/02/2020/7630/GLOCKE-SpielraumWinterferien-Buehnenreif', 'description': ''},
        {'type': 'film', 'day': '', 'location': 'Atlantis ', 'time': '14:00', 'title': 'Das Vorspiel KINOTAG', 'url': 'http://www.bremerfilmkunsttheater.de/Kino_Reservierungen/Atlantis.html ', 'description': ''},
        {'type': 'film', 'day': '', 'location': 'Schauburg', 'time': '15:00', 'title': 'Jojo Rabbit KINOTAG', 'url': 'http://www.bremerfilmkunsttheater.de/Kino_Reservierungen/Schauburg.html', 'description': 'Für Jojo Betzler aus dem idyllischen Städtchen Falkenheim geht ein Traum in Erfüllung, dem er bereits seit 10 Jahren (...)'},
        {'type': 'film', 'day': '', 'location': 'Gondel', 'time': '15:00', 'title': 'Als Hitler das rosa Kaninchen stahl KINOTAG', 'url': 'http://www.bremerfilmkunsttheater.de/Kino_Reservierungen/Gondel.html ', 'description': ''},
    ]


@view_config(route_name='home', renderer='kulturweb:templates/home.pt')
def home_index(_):
    return {
        'shows': get_test_shows(),
        'filter': ''
    }


@view_config(route_name='filter/', renderer='kulturweb:templates/home.pt')
@view_config(route_name='filter', renderer='kulturweb:templates/home.pt')
def filter_shows(request: Request):
    when = request.matchdict.get('when')
    where = request.matchdict.get('where')
    options = request.matchdict.get('options')

    filter_keywords = 'start'

    if 'heute' in when:
        filter_keywords += 'today '
    if 'morgen' in when:
        filter_keywords += 'morgen '
    if 'uebermorgen' in when:
        filter_keywords += 'uebermorgen '
    if 'woche' in when:
        filter_keywords += 'woche '
    if 'kino' in where:
        filter_keywords += 'kino '
    if 'buehne' in where:
        filter_keywords += 'buehne '
    if 'musik' in where:
        filter_keywords += 'musik '
    if 'eingeschlossen' in options:
            filter_keywords += 'auch dubbed '
    if 'ausgeschlossen' in options:
                filter_keywords += 'nicht dubbed '

    return {
        'shows': get_test_shows(),
        'filter': filter_keywords,
    }
