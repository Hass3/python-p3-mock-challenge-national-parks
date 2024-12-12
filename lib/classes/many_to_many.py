
class NationalPark:
    all = []
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string or 3 or more chars long")
        self._name = name
        NationalPark.all.append(self)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if hasattr(self,"._name"):
            raise AttributeError("name cannot be changed")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self and isinstance(trip,Trip)]
    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips() if isinstance(trip.visitor, Visitor)]))
    
    def total_visits(self):
       return len(self.trips())
       
    def best_visitor(self):
        if len(self.visitors()) == 0:
            return None
        return max(self.visitors(), key=lambda x: x.total_visits_at_park(self))
     
    @classmethod
    def most_visited(cls):
        if  len(cls.all) == 0:
            return None
        return max(cls.all, key=lambda park: park.total_visits())

class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self,new_start_date):
        if isinstance(new_start_date, str) and len(new_start_date) >= 7 and (new_start_date.endswith("st") or new_start_date.endswith("nd") or new_start_date.endswith("rd") or new_start_date.endswith("th")) :
            self._start_date = new_start_date 
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self,value):
        if isinstance(value,str) and len(value) >=7 and (value.endswith("st") or value.endswith("nd") or value.endswith("rd") or value.endswith("th")) :
            self._end_date = value

    @property     
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self,visitor):
        if not isinstance(visitor,Visitor):
            raise Exception("Must be of the Visitor class")
        self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self,value):
        if not isinstance(value,NationalPark):
            raise Exception("Must be of the National Park class")
        self._national_park = value
    


class Visitor:
    all = []
    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (1<= len(name) <= 15):
            self._name = name

    def trips(self):
        return[trip for trip in Trip.all if trip.visitor == self and isinstance(trip, Trip)] 
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips() if isinstance(trip.national_park, NationalPark)]))
        
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])