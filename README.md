# Entrega1-FilippettiGian
Entrega 1 proyecto final de Coderhouse
El proyecto Adoptame Tandil surge en 2017 como una necesidad de reinsertar perros de zoonosis que tuvieron problemas de comportamientos hacia animales y personas.
A partir de ese momento un grupo de voluntarios , especialistas en comportamiento canino y veterinarios trabajan de manera conjunta para cumplir estos objetivos.
Finalmente dado que este curso tiene como objetivo generar una pagina web y Adoptame Tandil presentaba esta necesidad decidi encarar este proyecto con la finalidad de afianzar los conocimientos que fui adquiriendo durante el curso y mejorarlos para cumplir las necesidades de este objetivo y administrar su pagina como voluntario

En cuanto a la pagina web se puede encontrar:
Un html base que hace herencia a todas las vistas de la pagina , en este template se puede ver una navbar color naranja
(el naranja representa la lucha contra el maltrato animal) y un footer del mismo color ambos objetos fueron descargados de boostrap.
Los html relacionados a list_our_dogs , list_our_colaborative_institutions , list_our_volunteer y list_others_projects poseen una card descargada de boostrap donde:
se puede ver en el codigo que esta el boton 'Go somewhere' esta comentado dado que en un futuro se pretender generar una nueva vista donde se pueda poner mas informacion del asunto correspondiente
A su vez en el proyecto se comenzo a configurar todo para generar imagenes individuales de las distitnas views.
Las views (def list_our_dogs , def list_our_colaborative_institution , list_our_volunteer y list_others_projects) apuntan a los HTML mencionados arriba , estos archivos al tener un bucle for permiten generar una card para cada objeto.
A su vez en estas vistas , los botones colores verdes dirigen a las views create_our_dogs , create_our_volunteers , create_our_colaborative_institution y create_others_projects
los cuales apuntan a los archivos html create_our_dogs , create_our_volunteers , create_others projects y create_our_colaborative_institutions los cuales son formularios que si bien en un principio se hicieron a partir de codigo html , luego se opto por hacerlo con django generando un archivo forms.py dado que son mas seguros que los html
Por ultimo los modelos se relacionan a las necesidades de Adoptame Tandil dado que esta organizacion presenta perros , voluntarios , nuevos proyectos que se estan generando y en un futuro instituciones colaborativas los cuales todos merecen ser mencionados.

Algunos errores encotnrados durante la confeccion y a corregir en la proxima entrega:
1) Los colores naranjas del footer y navbar no coinciden , se buscara encajar mejor ambos colores dado que ya estan configurados
2) El footer le falta completar su configuracion y pasar todos los colores de las letras a negro
3) Al generar un nuevo voluntario-institucion-perro o proyecto el footer se levanta esto fue corregido generando <br> para dar salto de lineas pero se buscara una mejor manera
4) la navbar siempre apunta su busqueda a la base de datos relacionado a los perros , se buscara en un futuro que la busqueda se amplie a los 4 modelos
5) los formularios estan en ingles sin embargo esto se puede solucionar generando un par de configuraciones en settings.
