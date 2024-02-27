Descripción del problema:

El Fondo Nacional de Salud (FONASA) enmarcado en el proceso de Transformación Digital ha
tomado la decisión de automatizar la atención al paciente de los diferentes hospitales de la Región
Metropolitana. Cada hospital cuenta con varias consultas, de una consulta se controla el Id de la
misma, la cantidad de pacientes atendidos, el nombre del especialista que la atiende, el estado de la
consulta que puede ser ocupada o en espera de atención al paciente y el tipo de consulta (Pediatría,
Urgencia ó CGI (Consulta General Integral)).

En cada hospital se divide la atención de los pacientes de acuerdo a su edad en: niño (1-15 años),
joven (16-40 años) y anciano (41 en adelante). De los pacientes al hospital le interesa registrar su
nombre, edad y el número de historia clínica. En el caso de los niños se controla además la relación
peso-estatura (valor entre 1-4), de los jóvenes se necesita conocer si es fumador o no, además los
años que lleva de fumador, que pueden ser un valor entre (0 ó n) en dependencia de si es fumador o
no y de los ancianos, si tiene dieta asignada.

El hospital le asigna a cada paciente una prioridad para su atención, que se determina teniendo en
cuenta lo siguiente:

Para los niños:
- (1-5 años)
Peso-estatura + 3
- (6-12 años)
Peso-estatura + 2
- (13-15 años)
Peso-estatura + 1

Para los jóvenes:
- Si es fumador: Años de fumador/4 + 2
- En cualquier otro caso: 2
Para los ancianos:

- Si tiene dieta y está entre 60 y 100 años: Edad/20 + 4
Si no:
Edad/30 + 3
Además, se sabe que cada paciente tiene un riesgo que se determina por:
- (Edad * prioridad) / 100.
Y en el caso de los ancianos:
- (Edad * prioridad)/100 + 5.3
La atención de un paciente se realiza respecto a su prioridad (los de mayor prioridad primero), para
esto se analiza si existe alguna consulta para su atención (el estado de la consulta debe ser
desocupada). En el caso de ser niño con prioridad menor ó igual a 4, sólo pueden ser atendidos en
una consulta de pediatría, los jóvenes y los ancianos se atenderán en la consulta de CGI, en la
consulta de urgencia se atenderán a los pacientes con prioridad mayor que 4 independientemente de
la edad. Se debe tener en cuenta que si no existe consulta disponible para atender al paciente de la
sala de pendientes, este pasará para una sala de espera donde al igual serán atendidos en dependencia
de su prioridad.

El flujo de actividades para la atención al paciente es el siguiente:

1. Atender todos los pacientes en la sala de espera que sea posible dada la disponibilidad de
consultas.
2. Si la sala de espera está vacía (inicialmente o luego de atender a los pacientes en espera) se
atienden los pacientes pendientes según su prioridad y orden de llegada.
3. Si luego de atendidos los de la sala de espera no quedara ninguna consulta libre, entonces
el paciente de la sala de pendiente que le corresponde ser atendido según su prioridad, pasa a la sala
de espera, sino será atendido por la consulta adecuada.

Descripción del sistema:

Requisitos:

• Implementar la funcionalidad Listar_Pacientes_Mayor_Riesgo. Esta funcionalidad
consiste en, dado un número de historia clínica, listar todos los pacientes con mayor riesgo
que el del paciente al que pertenece el número de historia clínica dado.
• Implementar la funcionalidad Atender_Paciente, teniendo en cuenta la descripción del
proceso en el enunciado del problema.
• Implementar la funcionalidad Liberar_Consultas. Esta funcionalidad libera todas las
consultas que están ocupadas en el Hospital. Para esta funcionalidad hay que tener en cuenta
que una vez que se liberen todas las consultas se procede a atender a los pacientes que estén
en sala de espera.
• Implementar la funcionalidad Listar_Pacientes_Fumadores_Urgentes que consiste
en listar el nombre de los pacientes fumadores que necesitan ser atendidos con urgencia.
• Implementar la funcionalidad Consulta_mas_Pacientes_Atendidos que consiste en
mostrar la consulta que más pacientes ha atendido hasta el momento del pedido.
• De los pacientes que están en la sala de espera se necesita saber cuál es el más anciano de
todos. Implementar la funcionalidad Paciente_Mas_Anciano.

• Implementar la funcionalidad Optimizar_Atención que consiste en optimizar la atención al
paciente. En aras de que el paciente salga satisfecho de la clínica, se reorganizarán de forma
tal que queden organizados de forma óptima. Para esto los pacientes de mayor gravedad, en
orden de urgencia, quedarán en el inicio, los niños y ancianos a continuación por prioridad
y orden de llegada y por último los jóvenes más sanos. Los pacientes que se encuentren en
la sala de espera serán ubicados según su orden original, siempre teniendo en cuenta su
prioridad y urgencia. Luego de organizada la cola de atención se procede a atender los
pacientes posibles, es decir, todos los posibles dada la disponibilidad de consultas sin realizar
ubicaciones en la sala de espera. Finalmente se cambia el estado de todas las consultas
ocupadas a libre.
