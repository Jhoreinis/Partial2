# Parking Lot
Partial2
Explicación UML:
Para la implementación de este UML se creó una clase abstracta llamada Parqueadero con cuatro atributos necesarios y tres metodos que llevan acabo la funcionalidad del problema, adicional a esto se creó tres subclases que heredan de la clase abstracta los metodos y atributos a exepción de dos atributos adicionales propios de cada subclases. Se utilizó una clase abstracta para evitar repetir codigo y adicional a esto se utilizó ya que era necesario que cada subclase implementara la funcionalidad o cada metodo de forma diferente, por esta razón las subclases tienen la flecha que indica que heredan algo de la clase abstracta.

Explicacion codigo:

Se creó una clase abstracta ya que es necesario tener subclases que implementen de forma diferen cada metodo porque hay tres tipos de autos diferentes
Cada subclase implementa la funcionalidad y supone que ya hay usuarios registrados, es decir que al ejecutar el codigo arrojará la cantidad de plazas disponibles pero no indicará si ya la cantidad de plazas están llenas y que no es posible que un usuario nuevo ingrese, ya que cada metodo de las subclase va desde i hasta la cantidad de usuarios registrados. Es necesario ingresar el numero de horas que cada usuario registrado.
