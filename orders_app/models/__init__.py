from .clients import Clients
from .stocks import Stocks
from .units import Units
from .carriers import Carriers
from .trucks import Trucks
from .drivers import Drivers

for __all__ in [Clients, Stocks, Units, Carriers, Trucks, Drivers]:
    __all__.objects.all()
