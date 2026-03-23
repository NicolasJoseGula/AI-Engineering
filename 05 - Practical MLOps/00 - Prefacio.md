Ambos hemos dedicado la mayor parte de nuestras carreras a automatizar procesos. Cuando nos conocimos y Alfredo no sabía Python, Noah sugirió automatizar una tarea por semana. La automatización es un pilar fundamental de MLOps, DevOps y de este libro en su totalidad. Debes considerar todos los ejemplos y opiniones de este libro en el contexto de la automatización futura.

Si Noah tuviera que resumir cómo pasó el periodo de 2000 a 2020, diría que se dedicó a automatizar prácticamente todo lo que pudo, desde la producción de películas hasta la instalación de software y los procesos de aprendizaje automático. Como gerente de ingeniería y director de tecnología en startups del Área de la Bahía, creó numerosos equipos de ciencia de datos desde cero. Como resultado, pudo observar muchos de los problemas fundamentales para la implementación del aprendizaje automático en producción durante las primeras etapas de la revolución de la IA/ML.

En los últimos años, Noah ha sido profesor adjunto en Duke, Northwestern y UC Davis, impartiendo clases sobre temas centrados principalmente en la computación en la nube, la ciencia de datos y la ingeniería de aprendizaje automático. Esta experiencia docente y laboral le brinda una perspectiva única sobre los desafíos que implica la implementación práctica de soluciones de aprendizaje automático.

Alfredo cuenta con una sólida experiencia en operaciones, adquirida durante su etapa como administrador de sistemas, y comparte su pasión por la automatización. Para él, es imposible construir una infraestructura resiliente sin automatización mediante comandos de voz. No hay nada más gratificante en situaciones de desastre que volver a ejecutar un script o un proceso para recrear el fallo.

Cuando llegó la COVID-19, se aceleró una pregunta que ambos teníamos: "¿Por qué no estamos implementando más modelos en producción?". Noah abordó algunos de estos temas en un [artículo que escribió para Forbes](https://oreil.ly/Qj8ut) . La premisa principal del artículo es que algo falla en la ciencia de datos porque las organizaciones no están obteniendo un retorno de sus inversiones.

Más tarde, en el [evento “Foo Camp” de O’Reilly](https://oreil.ly/ODJvG) , Noah dirigió una sesión sobre “¿Por qué no podemos ser diez veces más rápidos en el aprendizaje automático en producción?”, donde tuvimos un interesante debate con muchas personas, entre ellas Tim O’Reilly, Mike Loukides, Roger Magoulas y otros. La conclusión fue: “Sí, podemos ser diez veces más rápidos”. Así que gracias a Tim y Mike por propiciar un debate tan fascinante y por hacer posible la publicación de este libro.

El aprendizaje automático se parece mucho a otras tecnologías surgidas en las últimas décadas. Al principio, se necesitan años para obtener resultados. Steve Jobs habló de cómo NeXT quería acelerar diez veces la creación de software (y lo consiguió). Puedes ver la entrevista en [YouTube . ¿Cuáles son algunos de los problemas](https://oreil.ly/mWRoO) actuales del aprendizaje automático ?

- Concéntrese en el "código" y los detalles técnicos en lugar del problema empresarial.
- Falta de automatización
- HiPPO (Opiniones de la persona mejor pagada)
- No es nativo de la nube
- Falta de urgencia para resolver problemas que tienen solución.

Citando uno de los puntos que Noah mencionó en la discusión: “Estoy en contra del elitismo en todos los sentidos. La programación es un derecho humano. La idea de que exista una élite privilegiada para programar es simplemente errónea”. Al igual que con el aprendizaje automático, es fundamental que la tecnología esté únicamente en manos de un grupo selecto. Con MLOps y AutoML, estas tecnologías pueden estar al alcance de todos. Podemos mejorar el aprendizaje automático y la inteligencia artificial democratizando esta tecnología. Los profesionales de IA/ML implementan modelos en producción, y en el futuro, personas como médicos, abogados, mecánicos y profesores utilizarán la IA/ML para facilitar su trabajo.

# Cómo está organizado este libro
Diseñamos este libro para que cada capítulo se pueda leer de forma independiente y te brinde ayuda inmediata. Al final de cada capítulo encontrarás preguntas para la reflexión que buscan estimular el pensamiento crítico y ejercicios técnicos para mejorar tu comprensión del material.

Estas preguntas y ejercicios de debate son ideales para su uso en el aula, tanto en programas de Ciencia de Datos, Informática o MBA, como para el autodidacta motivado. El último capítulo incluye varios estudios de caso útiles para desarrollar un portafolio profesional como experto en MLOps.

El libro está dividido en 12 capítulos, que analizaremos con más detalle en la siguiente sección. Al final del libro, se incluye un apéndice con una recopilación de recursos valiosos para la implementación de MLOps.

## Capítulos
Los primeros capítulos abarcan la teoría y la práctica de DevOps y MLOps. Entre los temas tratados se encuentra la configuración de la integración continua y la entrega continua. Otro tema fundamental es Kaizen, es decir, la idea de la mejora continua en todos los ámbitos.

Hay tres capítulos sobre computación en la nube que abarcan AWS, Azure y GCP. Alfredo, defensor de desarrolladores de Microsoft, es una fuente de conocimiento ideal para MLOps en la plataforma Azure. Asimismo, Noah ha dedicado años a capacitar a estudiantes en computación en la nube y a colaborar con los departamentos de formación de Google, AWS y Azure. Estos capítulos son una excelente manera de familiarizarse con MLOps en la nube.

Otros capítulos abarcan áreas técnicas cruciales de MLOps, como AutoML, contenedores, computación perimetral y portabilidad de modelos. Estos temas incluyen numerosas tecnologías emergentes de vanguardia con gran aceptación.

Finalmente, en el último capítulo, Noah presenta un estudio de caso real sobre su experiencia en una empresa emergente de redes sociales y los desafíos que enfrentaron al implementar MLOps.

## Apéndices
Los apéndices son una recopilación de ensayos, ideas y valiosos elementos surgidos en los años transcurridos entre la finalización _de Python for DevOps_ (O'Reilly) y la publicación de este libro. Su principal utilidad reside en ayudarte a tomar decisiones sobre el futuro.

## Preguntas de ejercicio
En los ejercicios de este libro, una útil heurística explica cómo integrarlos en un portafolio utilizando GitHub y un tutorial en YouTube que muestre el proceso. Como dice el dicho, «una imagen vale más que mil palabras», un enlace de YouTube a un tutorial de un proyecto reproducible de GitHub en un currículum puede valer 10 000 palabras y elevar la calificación del currículum a un nuevo nivel para un puesto de trabajo.

A medida que avances en el libro y realices los ejercicios, ten en cuenta el siguiente marco de pensamiento crítico.

## Preguntas para el debate
Según Jonathan Haber en su libro _Pensamiento crítico_ (serie Conocimiento esencial de MIT Press) y la fundación sin fines de lucro [Foundation for Critical Thinking](https://oreil.ly/FXoTU) , las preguntas de debate son componentes esenciales del pensamiento crítico. El mundo necesita urgentemente pensamiento crítico debido a la proliferación de desinformación y contenido superficial en las redes sociales. Dominar las siguientes habilidades distingue a una persona del resto:

Humildad intelectual
	Reconocimiento de los límites de tu conocimiento.

Coraje intelectual
	La capacidad de defender tus creencias incluso frente a la presión social.

Empatía intelectual
	La capacidad de ponerse en el lugar de los demás para comprender su postura.

Autonomía intelectual
	La capacidad de pensar por uno mismo, independientemente de los demás.

Integridad intelectual
	La capacidad de pensar y argumentar con los mismos estándares intelectuales que esperas que los demás te apliquen.

Perseverancia intelectual
	La capacidad de aportar pruebas que respalden su postura.

Confianza en la razón
	La creencia de que existen hechos indiscutibles y que la razón es la mejor solución para adquirir conocimiento.

Imparcialidad
	La capacidad de esforzarse de buena fe por tratar todos los puntos de vista con imparcialidad.

Utilizando estos criterios, evalúe las preguntas de debate de cada capítulo.

