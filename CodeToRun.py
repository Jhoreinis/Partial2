from CocheCars import CocheCars
from CocheVan import CocheVan
from CocheSuv import CocheSuv

parqueo = CocheCars(10, 10, 10, "compacto", 5, 1000)
parqueo.horario()
parqueo.cobrohoras()
parqueo.plazas()


parqueo = CocheVan(10, 10, 10, "van", 5, 2000)
parqueo.horario()
parqueo.cobrohoras()
parqueo.plazas()

parqueo = CocheSuv(10, 10, 10, "suv", 5, 3000)
parqueo.horario()
parqueo.cobrohoras()
parqueo.plazas()