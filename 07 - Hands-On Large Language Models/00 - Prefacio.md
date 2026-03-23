Grandes modelos de lenguaje (LLM)Han tenido un impacto profundo y de gran alcance en el mundo. Al permitir que las máquinas comprendan mejor y generen un lenguaje similar al humano, los sistemas de aprendizaje automático han abierto nuevas posibilidades en el campo de la IA y han impactado a industrias enteras.

Este libro ofrece una introducción completa y muy visual al mundo de los modelos de lenguaje natural (MLN), abarcando tanto los fundamentos conceptuales como las aplicaciones prácticas. Desde las representaciones de palabras que precedieron al aprendizaje profundo hasta la arquitectura Transformer, de vanguardia en el momento de escribir este libro, exploraremos la historia y la evolución de los MLN. Profundizaremos en su funcionamiento interno, analizando sus arquitecturas, métodos de entrenamiento y técnicas de ajuste fino. También examinaremos diversas aplicaciones de los MLN en clasificación de texto, agrupamiento, modelado de temas, chatbots, motores de búsqueda y mucho más.

Con su singular combinación de desarrollo de la intuición, aplicaciones prácticas y estilo ilustrativo, esperamos que este libro proporcione la base ideal para quienes deseen explorar el apasionante mundo de los  LLM. Tanto si eres principiante como experto, te invitamos a unirte a nosotros en este viaje para comenzar a desarrollarte profesionalmente con LLMs.

# Una filosofía que prioriza la intuición
Elprincipa objetivo de este libro es ofrecer una _introducción intuitiva_ al campo de los LLM (Maestrías en Lenguaje). El ritmo de desarrollo en el campo de la IA del lenguaje es increíblemente rápido, y puede resultar frustrante intentar mantenerse al día con las últimas tecnologías. Por ello, nos centramos en los fundamentos de los LLM y pretendemos ofrecer un proceso de aprendizaje ameno y sencillo.

Para lograr esta filosofía [que](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/preface01.html#ch01fn1) _prioriza la intuición,_ utilizamos profusamente el lenguaje visual. Las ilustraciones ayudarán a dar una identidad visual a los conceptos y procesos clave del aprendizaje de los másteres en Derecho (LLM). Con nuestro método ilustrativo de narración, queremos invitarte a un viaje por este campo apasionante y con el potencial de transformar el mundo.

A lo largo del libro, establecemos una clara distinción entre modelos de lenguaje de representación y generativos. Los modelos de representación son modelos de lenguaje que no generan texto, pero se utilizan comúnmente para casos de uso específicos, como la clasificación, mientras que los modelos de generación son modelos de lenguaje que sí generan texto, como los modelos GPT. Si bien los modelos generativos suelen ser lo primero que viene a la mente al pensar en modelos de lenguaje, los modelos de representación siguen siendo muy útiles. Además, utilizamos el término "grande" de forma imprecisa al referirnos a _modelos de lenguaje grandes_ y a menudo optamos por llamarlos simplemente modelos de lenguaje, ya que las descripciones de tamaño suelen ser bastante arbitrarias y no siempre indican su capacidad.


# Requisitos previos
Este libro presupone que tienes cierta experiencia programando en Python y que conoces los fundamentos del aprendizaje automático. El enfoque se centra en desarrollar una sólida intuición, más que en derivar ecuaciones matemáticas. Por ello, las ilustraciones combinadas con ejemplos prácticos guiarán el aprendizaje a lo largo del libro. Este libro no requiere conocimientos previos de marcos de aprendizaje profundo populares como PyTorch o TensorFlow, ni de modelado generativo.

Si no está familiarizado conPython, un excelente lugar para comenzar es [Learn Python](https://oreil.ly/arcIm) , donde encontrarás muchos tutoriales sobre los fundamentos del lenguaje. Para facilitar aún más el proceso de aprendizaje, hemos puesto todo el código a tu disposición.en [Google Colab](https://oreil.ly/kSucO) , una plataforma donde puedes ejecutar todo el código sin necesidad de instalar nada localmente.

# Estructura del libro
El libro se divide en tres partes principales. Estas se ilustran en [la Figura P-1](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/preface01.html#all_parts_and_chapters_of_the_bookdot) para que pueda ver el libro completo. Tenga en cuenta que cada capítulo se puede leer de forma independiente, así que no dude en hojear los capítulos que ya conozca.

## Parte I: Comprensión de los modelos lingüísticos
En la primera parte del libro, exploramos el funcionamiento interno de los modelos de lenguaje, tanto pequeños como grandes. Comenzamos con una descripción general del campo y las técnicas comunes (véase [el Capítulo 1](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch01.html#an_introduction_to_large_language_model) ) antes de abordar dos componentes centrales de estos modelos: la tokenización y las incrustaciones (véase [el Capítulo 2](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch02.html#tokens_and_embeddings) ). Finalizamos esta parte con una versión actualizada y ampliada del conocido [Transformador Ilustrado](https://oreil.ly/UI4lN) de Jay , que profundiza en la arquitectura de estos modelos (véase [el Capítulo 3](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch03.html#looking_inside_large_language_models) ). Se presentarán numerosos términos y definiciones que se utilizarán a lo largo del libro.

![[Pasted image 20260322232246.png]]

## Parte II: Uso de modelos de lenguaje preentrenados
En la segunda parte del libro, exploramos cómo se pueden utilizar los modelos de lógica difusa (LLM) mediante casos de uso comunes. Utilizamos modelos preentrenados y demostramos sus capacidades sin necesidad de ajustarlos.

Aprenderás a utilizar modelos de lenguaje para la clasificación supervisada (véase [el capítulo 4](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch04.html#text_classification) ), la agrupación de textos y el modelado de temas (véase [el capítulo 5](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch05.html#text_clustering_and_topic_modeling) ), el aprovechamiento de modelos de incrustación para la búsqueda semántica (véase [el capítulo 6](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch06.html#prompt_engineering) ), la generación de texto (véanse los capítulos [7](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch07.html#advanced_text_generation_techniques_and) y [8](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch08.html#semantic_search_and_retrieval_augmented) ) y la ampliación de las capacidades de generación de texto al dominio visual (véase [el capítulo 9](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch09.html#multimodal_large_language_models) ).

Aprender las capacidades de estos modelos de lenguaje individuales te proporcionará las habilidades necesarias para resolver problemas con modelos de lenguaje y construir sistemas y flujos de trabajo cada vez más avanzados.

## Parte III: Entrenamiento y ajuste fino de modelos de lenguaje
En la Parte III del libro, exploraremos conceptos avanzados mediante el entrenamiento y el ajuste fino de todo tipo de modelos de lenguaje. Analizaremos cómo crear y ajustar un modelo de incrustación (véase [el Capítulo 10](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch10.html#creating_text_embedding_models) ), revisaremos cómo ajustar BERT para la clasificación (véase [el Capítulo 11](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch11.html#fine_tuning_representation_models_for_c) ) y finalizaremos el libro con varios métodos para ajustar modelos de generación (véase [el Capítulo 12](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch12.html#fine_tuning_generation_models) ).

# Requisitos de hardware y software
Ejecutar modelos generativos es generalmente una tarea computacionalmente intensiva que requiere una computadora con una GPU potente. Dado que no todos los lectores tienen acceso a ellas, todos los ejemplos de este libro están diseñados para ejecutarse utilizando una plataforma en línea, concretamente [Google Colaboratory](https://oreil.ly/HQawv) , a menudo abreviado comoa “Google Colab”. En el momento de escribir esto, esta plataforma le permite usar unaGPU NVIDIA (T4) gratuita para ejecutar tu código. Esta GPUtiene 16 GB deVRAM (que es la memoria de tu GPU), que es la cantidad mínima de VRAM que esperamos para los ejemplos a lo largo del libro.

Todo el código, los requisitos y los tutoriales adicionales estánDisponible en [el repositorio de este libro](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) . Si desea ejecutar los ejemplos localmente, recomendamos tener acceso a una GPU NVIDIA con un mínimo de 16 GB de VRAM. Para una instalación local, por ejemplo con conda, puede seguir esta configuración para crear su entorno:

```
conda create -n thellmbook python=3.10 
conda activate thellmbook
```

Puedes instalar todas las dependencias necesarias bifurcando o clonando el repositorio y luego ejecutando lo siguiente en tu entorno Python 3.10 recién creado:

```
pip install -r requirements.txt
```

# Claves API

En los ejemplos utilizamos modelos tanto de código abierto como propietarios para demostrar las ventajas y desventajas de ambos. Para los modelos propietarios, que utilizan la oferta de OpenAI y Cohere, deberá crear una cuenta gratuita:

[OpenAI](https://oreil.ly/M4nAa)
Hacer clicRegístrate en el sitio para crear una cuenta gratuita. Esta cuenta te permite generar una clave API, que podrás usar para acceder a GPT-3.5. Luego, ve a "Claves API" para crear una clave secreta.

[Cohere](https://oreil.ly/T63GA)
RegistroCrea una cuenta gratuita en el sitio web. Luego, ve a “Claves API” para crear una clave secreta.

Tenga en cuenta que, en ambos casos, se aplican límites de velocidad y que estas claves API gratuitas solo permiten un número limitado de llamadas por minuto. En todos los ejemplos, hemos considerado esta limitación y proporcionado alternativas locales cuando ha sido necesario.

Para los modelos de código abierto, no es necesario crear una cuenta, con la excepción del modelo Llama 2.en [el Capítulo 2.](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/ch02.html#tokens_and_embeddings) Para usar ese modelo, necesitarás una cuenta de Hugging Face:

[Hugging Face](https://oreil.ly/_uV3A)'
Hacer clicRegístrate en el sitio web de Hugging Face para crear una cuenta gratuita. Luego, en "Configuración", ve a "Tokens de acceso" para crear un token que podrás usar para descargar ciertos LLM.

