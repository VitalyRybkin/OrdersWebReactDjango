from .clients import Clients
from .stocks import Stocks
from .units import Units
from .carriers import Carriers
from .trucks import Trucks
from .drivers import Drivers
from .truck_types import TruckTypes
from .truck_capacities import TruckCapacities


for __all__ in [Clients, Stocks, Units, Carriers, Trucks, Drivers, TruckTypes, TruckCapacities]:
    __all__.objects.all()
