# class OwnerRequest:
#     def __init__(self, location):
#         self.location = location
        
# class Landfields:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
        
# class LandfieldsManager:
#     def __init__(self):
#         self.landfields = [] # list of landfields
        
#     def add_landfield(self, landfield):
#         self.landfields.append(landfield)
        
#     def nearest_landfield(self, landfield):
#         min_distance = float('inf')
#         closest_landfield = None
#         for landfield in self.landfields:
#             distance = self.calculate_distance(landfield.location, landfield.location)
#             if distance < min_distance:
#                 min_distance = distance
#                 closest_landfield = landfield
#         return closest_landfield
    
    
    
import math

class OwnerRequest:
    def __init__(self, location):
        self.location = location
        
class Landfields:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
class LandfieldsManager:
    def __init__(self):
        self.landfields = [] # list of landfields

    def haversine(self, loc1, loc2):
        R = 6371  # radius of Earth in kilometers
        lat1, lon1 = loc1
        lat2, lon2 = loc2
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def add_landfield(self, landfield):
        self.landfields.append(landfield)
        
    def nearest_landfield(self, owner_request):
        min_distance = float('inf')
        closest_landfield = None
        for landfield in self.landfields:
            distance = self.haversine(owner_request.location, landfield.location)
            if distance < min_distance:
                min_distance = distance
                closest_landfield = landfield
        return closest_landfield
    
    
# Example test

# Create an instance of LandfieldsManager
manager = LandfieldsManager()

# Add landfields
manager.add_landfield(Landfields('Landfield1', (10.0, 10.0)))
manager.add_landfield(Landfields('Landfield2', (20.0, 20.0)))
manager.add_landfield(Landfields('Landfield3', (30.0, 30.0)))

# Create an OwnerRequest
request = OwnerRequest((150.0, 151.0))

# Find the nearest landfield
nearest_landfield = manager.nearest_landfield(request)

# Print the name of the nearest landfield
print(nearest_landfield.name)

    