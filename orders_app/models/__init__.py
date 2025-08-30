from .clients import Client
from .stocks import Stock
from .units import Unit
from .carriers import Carrier
from .trucks import Truck
from .drivers import Driver
from .truck_types import TruckType
from .truck_capacities import TruckCapacity
from .products import Product


for __all__ in [
    Client,
    Stock,
    Unit,
    Carrier,
    Truck,
    Driver,
    TruckType,
    TruckCapacity,
    Product,
]:
    __all__.objects.all()
