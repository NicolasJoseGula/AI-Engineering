La humanidad se encuentra en un punto de inflexión.DeA partir de 2012, el desarrollo de sistemas de IA (mediante redes neuronales profundas) se aceleró, de modo que, a finales de la década, se creó el primer sistema de software capaz de escribir artículos indistinguibles de los escritos por humanos. Este sistema era un modelo de IA llamado Generative Pre-trained Transformer 2, o GPT-2.2022 marcó el lanzamiento deChatGPT demostró el profundo potencial de esta tecnología para revolucionar nuestra interacción con la tecnología y la información. Alcanzando un millón de usuarios activos en cinco días y cien millones en dos meses, esta nueva generación de modelos de IA comenzó como chatbots con apariencia humana, pero rápidamente evolucionó hacia un cambio trascendental en nuestra forma de abordar tareas cotidianas como la traducción, la generación de texto, el resumen y mucho más. Se convirtió en una herramienta indispensable para programadores, educadores e investigadores.

El éxito de ChatGPT fue sin precedentes e impulsó la investigación sobre la tecnología subyacente, concretamente los modelos de lenguaje a gran escala (LLM). Se lanzaron modelos, tanto propietarios como públicos, a un ritmo constante, acercándose y, finalmente, igualando el rendimiento de ChatGPT. No es exagerado afirmar que casi toda la atención se centró en los LLM.

Como resultado, 2023 siempre será conocido, al menos para nosotros, como el año que cambió drásticamente nuestro campo, La Inteligencia Artificial del Lenguaje (IA del Lenguaje) es un campo caracterizado por el desarrollo de sistemas capaces de comprender y generar lenguaje humano.

Sin embargo, los modelos de lenguaje natural (LLM) existen desde hace tiempo y los modelos más pequeños siguen siendo relevantes hoy en día. Los LLM son mucho más que un solo modelo, y existen muchas otras técnicas y modelos en el campo de la IA del lenguaje que vale la pena explorar.

En este libro, nuestro objetivo es brindar a los lectores una sólida comprensión de los fundamentos tanto de los másteres en lenguaje natural (LLM) como del campo de la inteligencia artificial del lenguaje en general. Este capítulo sirve de base para el resto del libro e introduce conceptos y términos que utilizaremos a lo largo de los capítulos.

Pero, sobre todo, en este capítulo pretendemos responder a las siguientes preguntas:
- ¿Qué es la IA del lenguaje?
- ¿Qué son los modelos de lenguaje a gran escala?
- ¿Cuáles son los casos de uso y las aplicaciones más comunes de los modelos de lenguaje a gran escala?
- ¿Cómo podemos utilizar nosotros mismos los modelos de lenguaje a gran escala?

# ¿Qué es la IA del lenguaje?

Eltérmino _inteligencia artificial_ (IA)Se utiliza a menudo para describir sistemas informáticos dedicados a realizar tareas similares a la inteligencia humana, como el reconocimiento de voz, la traducción de idiomas y la percepción visual. Se trata de la inteligencia del software, en contraposición a la inteligencia humana.

He aquí una definición más formal proporcionada por uno de los fundadores de la disciplina de la inteligencia artificial:

> La inteligencia artificial es la ciencia y la ingeniería que se dedica a la creación de máquinas inteligentes, especialmente programas informáticos inteligentes. Se relaciona con la tarea similar de usar computadoras para comprender la inteligencia humana, pero la IA no tiene por qué limitarse a métodos biológicamente observables. John McCarthy, 2007 [1](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#ch01fn2)

Pendiente Debido a la naturaleza en constante evolución de la IA, el término se ha utilizado para describir una amplia variedad de sistemas, algunos de los cuales podrían no encarnar realmente un comportamiento inteligente. Por ejemplo, los personajes de los videojuegos. A los NPCs [nonplayable characters] a menudo se les denomina IA, aunque muchos no son más que sentencias condicionales _(if-else)_ .

La IA del lenguaje se refiere a un subcampo de la IA que se centra en el desarrollo de tecnologías capaces de comprender, procesar y generar lenguaje humano. El término _IA del lenguaje_ se puede usar a menudo indistintamente.con _el procesamiento del lenguaje natural_ (PLN) y el éxito continuado de los métodos de aprendizaje automático para abordar los problemas del procesamiento del lenguaje.

Utilizamos el término _IA del lenguaje_ para abarcar tecnologías que técnicamente podrían no ser LLM pero que aún así tienen un impacto significativo en el campo, como por ejemplo cómo los sistemas de recuperación pueden otorgar superpoderes a los LLM (véase [el Capítulo 8](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch08.html#semantic_search_and_retrieval_augmented) ).

A lo largo de este libro, nos centraremos en los modelos que han desempeñado un papel fundamental en el desarrollo del campo de la IA del lenguaje. Esto implica explorar más allá de los modelos de lenguaje a gran escala (LLMs) de forma aislada. Esto nos lleva a la siguiente pregunta: ¿qué son los MLE? Para comenzar a responderla en este capítulo, exploremos primero la historia de la IA del lenguaje.


# A Recent History of Language AI
La IA del lenguaje abarca muchos desarrollos y modelos que tienen como objetivo representar y generar lenguaje, como se ilustra en [la Figura 1-1](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#a_peek_into_the_history_of_language_aid) .

![[Pasted image 20260323002235.png]]

El lenguaje, sin embargo, es un concepto complejo para las computadoras. El texto es inherentemente no estructurado y pierde su significado al representarse mediante ceros y unos (caracteres individuales). Por consiguiente, a lo largo de la historia de la IA del lenguaje, se ha hecho especial hincapié en la representación estructurada del lenguaje para facilitar su uso por parte de las computadoras. En la [Figura 1-2](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#language_ai_is_capable_of_many_tasks_by) se muestran ejemplos de estas tareas de IA del lenguaje .

![[Pasted image 20260323002334.png]]

## Representar el lenguaje como una bolsa de palabras

La historia de la IA del lenguaje comienza con una técnica llamada bag-of-words (bolsa de palabras), un método para representar texto no estructurado. [2](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#ch01fn3) Se mencionó por primera vez alrededor de la década de 1950, pero se popularizó alrededor de la década de 2000.

El modelo de bolsa de palabras funciona de la siguiente manera: supongamos que tenemos dos oraciones para las cuales queremos crear representaciones numéricas. El primer paso del modelo de bolsa de palabras es _tokenización_ , el proceso de dividir las oraciones en palabras individuales o subpalabras ( _tokens_ ), como se ilustra en [la Figura 1-3](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#each_sentence_is_split_into_words_left) .

![[Pasted image 20260323002546.png]]

El método más común para la tokenización consiste en dividir las palabras por espacios en blanco. Sin embargo, esto tiene sus desventajas, ya que algunos idiomas, como el mandarín, no tienen espacios en blanco alrededor de las palabras. En el próximo capítulo, profundizaremos en la tokenización y cómo esta técnica influye en los modelos de lenguaje. Como se ilustra en [la Figura 1-4](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#a_vocabulary_is_created_by_retaining_al) , después de la tokenización, combinamos todas las palabras únicas de cada oración para crear un vocabulario que podemos usar para representarlas.

![[Pasted image 20260323002700.png]]

Utilizando nuestro vocabulario, simplemente contamos con qué frecuencia aparece una palabra en cada oración, creando literalmente una bolsa de palabras. Como resultado, un modelo de bolsa de palabras tiene como objetivo crear representaciones de texto en forma de números, también llamados vectores o representaciones vectoriales, observadas en la [Figura 1-5](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#a_bag_of_words_is_created_by_counting_i) . A lo largo del libro, nos referimos a este tipo de modelos como _modelos de representación_ .

![[Pasted image 20260323002825.png]]
Figura 1-5. Una bolsa de palabras se crea contando palabras individuales. Estos valores se denominan representaciones vectoriales.

Aunque el método de la bolsa de palabras es un método clásico, no está ni mucho menos completamente obsoleto. En el [capítulo 5](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch05.html#text_clustering_and_topic_modeling) , exploraremos cómo aún puede utilizarse para complementar lenguajes más recientes.modelos.

## Better Representations with Dense Vector Embeddings

Bag-of-words ,a pesar de este enfoque elegante tiene un defecto. Considera el lenguaje como nada más que un conjunto de palabras casi literales e ignora la naturaleza semántica, o el significado, del texto.

Lanzado en 2013, word2vec fue uno de los primeros intentos exitosos de capturar el significado del texto en _embeddings_ . [3](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#ch01fn4) Los _embeddings_ son representaciones vectoriales de datos que intentan capturar su significado. Para ello, word2vec aprende representaciones semánticas de las palabras entrenándose con grandes cantidades de datos textuales, como la totalidad de Wikipedia.

Para generar estas representaciones semánticas, word2vec aprovecha _Redes neuronales_ . Estas redes constan de capas interconectadas de nodos que procesan información. Como se ilustra en [la Figura 1-6](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#a_neural_network_consists_of_interconne) , las redes neuronales pueden tener muchas capas, donde cada conexión tiene un peso determinado que depende de la entrada. Estos pesos se conocen comúnmente como los _parámetros_ del modelo.

![[Pasted image 20260323003345.png]]Figura 1-6. Una red neuronal consta de capas interconectadas de nodos donde cada conexión es una ecuación lineal.

Utilizando estas redes neuronales, word2vec genera incrustaciones de palabras analizando con qué otras palabras tienden a aparecer junto a una oración dada. Comenzamos asignando a cada palabra de nuestro vocabulario una incrustación vectorial, por ejemplo, de 50 valores para cada palabra, inicializados con valores aleatorios. Luego, en cada paso de entrenamiento, como se ilustra en la [Figura 1-7](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#a_neural_network_is_trained_to_predic) , tomamos pares de palabras de los datos de entrenamiento y un modelo intenta predecir si es probable que aparezcan juntas en una oración.

Durante este proceso de entrenamiento, word2vec aprende la relación entre las palabras y destila esa información en la representación vectorial. Si dos palabras tienden a tener vecinos similares, sus representaciones vectoriales estarán más cerca entre sí, y viceversa. En el [Capítulo 2](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch02.html#tokens_and_embeddings) , analizaremos con más detalle el procedimiento de entrenamiento de word2vec.

![[Pasted image 20260323003830.png]]

Las representaciones vectoriales resultantes capturan el significado de las palabras, pero ¿qué significa eso exactamente? Para ilustrar este fenómeno, simplifiquemos un poco e imaginemos que tenemos representaciones vectoriales de varias palabras, concretamente «manzana» y «bebé». Estas representaciones intentan capturar el significado al representar las propiedades de las palabras. Por ejemplo, la palabra «bebé» podría tener una puntuación alta en las propiedades «recién nacido» y «humano», mientras que la palabra «manzana» tendría una puntuación baja en estas propiedades.

Como se ilustra en [la Figura 1-8](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#the_values_of_embeddings_represent_prop) , las incrustaciones pueden tener muchas propiedades para representar el significado de una palabra. Dado que el tamaño de las incrustaciones es fijo, sus propiedades se eligen para crear una representación mental de la palabra.
![[Pasted image 20260323004302.png]]
 Los valores de las incrustaciones representan propiedades que se utilizan para representar palabras. Si bien podemos simplificar demasiado imaginando que las dimensiones representan conceptos (lo cual no es cierto), esto ayuda a expresar la idea.

En la práctica, estas propiedades suelen ser bastante ambiguas y rara vez se relacionan con una sola entidad o concepto identificable por el ser humano. Sin embargo, en conjunto, estas propiedades tienen sentido para una computadora y sirven como una buena manera de traducir el lenguaje humano al lenguaje informático.

Las incrustaciones son tremendamente útiles, ya que nos permiten medir la similitud semántica entre dos palabras. Utilizando diversas métricas de distancia, podemos juzgar qué tan cerca está una palabra de otra. Como se ilustra en [la Figura 1-9](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#embeddings_of_words_that_are_similar_wi) , si comprimiéramos estas incrustaciones en una representación bidimensional, observaríamos que las palabras con significado similar tienden a estar más cerca. En [el Capítulo 5](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch05.html#text_clustering_and_topic_modeling) , exploraremos cómo comprimir estas incrustaciones en una representación _n-_ dimensional.espacio.

![[Pasted image 20260323004507.png]]

## Types of Embeddings
Hay muchos tipos de incrustaciones, como incrustaciones de palabras e incrustaciones de oraciones que se utilizan para indicar diferentes niveles de abstracción (palabra versus oración), como se ilustra en [la Figura 1-10](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#embeddings_can_be_created_for_different) .

Bag-of-words, por ejemplo, crea incrustaciones a nivel de documento ya que representa todo el documento. En cambio, word2vec genera incrustaciones solo para palabras.

A lo largo del libro, las incrustaciones desempeñarán un papel central, ya que se utilizan en numerosos casos prácticos, como **classification** (véase [el capítulo 4](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch04.html#text_classification) ), la **clustering** (véase [el capítulo 5](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch05.html#text_clustering_and_topic_modeling) ) y la retrieval-audmented generation y semantic search (véase [el capítulo 8](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch08.html#semantic_search_and_retrieval_augmented) ). En [el capítulo 2](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch02.html#tokens_and_embeddings) , profundizaremos por primera vez en el análisis de tokens incrustaciones.

![[Pasted image 20260323012023.png]]


