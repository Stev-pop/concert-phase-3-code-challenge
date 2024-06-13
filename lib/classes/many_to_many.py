class Band:
    all = []
    
    def __init__(self, name, hometown):
        self._name = name
        self._hometown = hometown
        Band.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value):
        raise AttributeError("Can't set attribute")

    def concerts(self):
        return [c for c in Concert.all if c.band == self]
    
    def venues(self):
        return list(set([concert.venue for concert in self.concerts()]))

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)
    
    def all_introductions(self):
        return list(concert.introduction() for concert in self.concerts())

class Concert:
    all = []
    
    def __init__(self, date, band, venue):
        self._date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    all = []
    
    def __init__(self, name, city):
        self._name = name
        self._city = city
        Venue.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value

    def concerts(self):
        return [c for c in Concert.all if c.venue == self]

    def bands(self):
        return list(set([concert.band for concert in self.concerts()]))
