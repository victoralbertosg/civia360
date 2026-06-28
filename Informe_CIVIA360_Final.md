# ESCUELA DE POSGRADO
## PROGRAMA ACADÉMICO DE MAESTRÍA EN INTELIGENCIA ARTIFICIAL

### Informe del Primer Avance del Producto Integrador Colaborativo (IF)

**Título:** CIVIA 360: Propuesta de Inteligencia Artificial Generativa para optimizar la atención de trámites, reclamos y orientación ciudadana en municipalidades.

**Curso:** Inteligencia Artificial Generativa
**Docente:** Mg. Sandra Nasheli Lozano Aragon
**Grupo:** 07
**Integrantes:**
- Medina Guevara, Maria Elena
- Rengifo Calvanapon, Ghandy Allizon
- Campos Ramos, Manuel Orlando
- Rios Espejo, Kervin Denis
- Soto Gutierrez, Victor Alberto

**Lima - Perú**
**2026**

---

## 1. INTRODUCCIÓN

### El laberinto de la ventanilla: diagnóstico y urgencia

Si algo caracteriza el día a día de nuestras municipalidades es, paradójicamente, la incertidumbre. Durante el tiempo que dedicamos a observar el flujo de atención en diversas comunas, lo que saltó a la vista no fue solo el papeleo, sino ese silencio frustrante que rodea al ciudadano que no sabe si su trámite llegará a buen puerto. No es una exageración decir que, hoy por hoy, la atención ciudadana en el Perú funciona como un rompecabezas cuyas piezas no siempre encajan: criterios que cambian según el turno, derivaciones infinitas y requisitos que aparecen —como por arte de magia— justo cuando el vecino cree haber terminado el proceso. ¿Cómo no va a haber desconfianza si, para obtener una simple licencia, alguien debe regresar tres veces a la misma oficina?

Esta es la grieta organizacional que CIVIA 360 pretende sellar. Tras analizar el núcleo del problema, entendimos que el caos no es solo falta de personal, sino un síntoma de algo más grave: el "conocimiento secuestrado". Tenemos instituciones donde la información vital vive en archivadores empolvados o, peor aún, únicamente en la memoria de funcionarios que, al rotar, se llevan consigo la eficiencia del área. Este diagnóstico nos lleva a una conclusión inevitable: el contrato social se desmorona en cada minuto de espera innecesaria. Es aquí donde la Inteligencia Artificial Generativa deja de ser una moda tecnológica para posicionarse como una herramienta de justicia administrativa, siempre y cuando, como advierte Bright et al. (2024), mantengamos un control humano que no se desvanezca tras el algoritmo.

### Fundamentos: De la máquina que calcula a la IA que interpreta

Para situar a CIVIA 360 en su justa dimensión, debemos despojarnos de la idea de que la IA es solo un buscador avanzado. Si miramos atrás, pasamos de sistemas de reglas rígidas a modelos de aprendizaje automático que identifican patrones. Pero lo que hoy tenemos entre manos, la IA Generativa, es un salto cualitativo. Hablamos de sistemas que ya no solo clasifican, sino que "razonan" sobre el lenguaje. Management Solutions (2024) acierta al decir que los LLM son el estado del arte de la computación lingüística, facilitando ahorros de tiempo que Microsoft ya sitúa en el umbral del 74 % para labores de oficina. Sin embargo, lo que nos parece realmente transformador es su capacidad para ser el puente entre el lenguaje técnico del TUPA y el lenguaje de a pie del vecino.

Ese puente solo es posible gracias a la arquitectura **Transformer**. Desde que Vaswani et al. (2017) publicaron su ya mítica idea de la **autoatención**, el procesamiento del lenguaje cambió de raíz: la máquina dejó de leer de corrido para empezar a entender qué palabras "pesan" más en una oración. Es lo que nos permite hoy conversar con un sistema y que este entienda el contexto. Pero —y este es un "pero" necesario— no ignoramos las sombras del camino. Las alucinaciones (Xu, 2024) y el peligroso **Efecto Eliza** (Porter et al., 2024), donde proyectamos humanidad en un código, nos obligan a ser cautelosos.

Por tal motivo, en CIVIA 360 no nos arriesgaremos con modelos abiertos que divagan. Nuestra apuesta es el **RAG (Generación Aumentada por Recuperación)**. La lógica es de un sentido común aplastante: antes de que la IA se atreva a responder, le obligamos a que busque la respuesta en nuestras ordenanzas oficiales (Lewis et al., 2020). Solo así la fluidez del lenguaje se ancla a la veracidad legal. Si esto se hace bien, como en las pruebas realizadas en entornos similares (Vera & Carrión, 2026), podemos aspirar a una precisión superior al 91 %, algo impensable hace solo un par de años.

### Propósito del informe

CIVIA 360 nace, entonces, no para reemplazar al servidor público, sino para dotarlo de un "superpoder" documental. El objetivo de este documento es trazar la ruta de este sistema: desde el diagnóstico de la ineficiencia hasta la arquitectura técnica que lo sostiene, analizando beneficios, riesgos éticos y esa necesaria gobernanza de datos que marcos como el AI Act de la UE ya nos exigen cumplir.

---

## 2. DESARROLLO

### Una radiografía del desorden municipal

Ciertamente, el problema de la atención ciudadana es estructural. En numerosas municipalidades peruanas, te encuentras con la paradoja de tener la información "en todos lados y en ninguno". Los requisitos están en el portal web, pero los criterios reales de aprobación están en la cabeza del jefe del área, y la actualización de los formatos suele ser un proceso que nadie comunica a tiempo. El resultado es el que todos conocemos: una dependencia enfermiza de la persona y no del proceso. 

Desde nuestro equipo consideramos que este desorden tiene un impacto directo en la legitimidad política. No solo se pierde dinero y tiempo (un costo económico que SAS, en 2025, califica de crítico para el sector público); se pierde la fe en la institución. Zhou et al. (2025) han sido claros en esto: el vecino no busca una IA que hable como poeta, busca una que le diga qué papel le falta y dónde lo entrega. Si Seattle (2025) ya está usando planes de IA para recuperar esa conexión con la comunidad, ¿por qué nosotros seguiríamos aferrados a ventanillas ancladas en el siglo XX?

### CIVIA 360: Relación de la IA con el problema real

Llegados a este punto, resulta imperativo explicar cómo la IA Generativa viene a rescatarnos de este caos. A diferencia del software tradicional, CIVIA 360 es capaz de "digerir" la complejidad de una ordenanza y explicarla sin perder el rigor. No estamos ante un chatbot de juguete; hablamos de un sistema tripartito: un motor de lenguaje potente, una biblioteca de vectores que guarda el TUPA con celo y, por supuesto, el filtro humano.

Esta sinergia nos permite proyectar cuatro campos de batalla. Primero, la orientación al ciudadano para evitar que camine por gusto. Segundo, el soporte al trabajador, dándole borradores que le ahorren horas de redacción repetitiva, lo que según Brynjolfsson et al. (2023) dispara la productividad en un 15 %. Tercero, la clasificación técnica: separar la paja del trigo para que lo urgente llegue a la mesa de quien decide de inmediato. Y cuarto, la minería gerencial: que el alcalde reciba cada lunes un reporte real de qué es lo que más le duele a su distrito.

Empero, el camino tiene espinas. No permitiremos que los datos del ciudadano se vuelvan mercancía o se expongan indebidamente. CIVIA 360 funcionará bajo reglas de anonimización quirúrgicas. Pero hay algo más: la IA no hará milagros si la municipalidad no limpia su casa. Como bien señala la OECD (2026), la tecnología solo amplifica la calidad de la información que ya tienes. Si tu ordenanza está mal escrita, CIVIA 360 te lo dirá con fluidez, pero seguirá estando mal. El reto, entonces, es tan tecnológico como institucional.

---

## 3. CONCLUSIONES

1.  Aceptamos que el gran muro de nuestras municipalidades no es la falta de datos, sino su dispersión. CIVIA 360 es la herramienta que proponemos para romper ese muro mediante el uso estratégico de la IA Generativa.
2.  La tecnología RAG se perfila como la única salvaguarda real para que el lenguaje fluido de las máquinas no se traduzca en desinformación administrativa, garantizando que cada respuesta tenga una base legal rastreable.
3.  Implementar este sistema es, en el fondo, una apuesta por la transparencia. Queremos que el ciudadano deje de ser un peregrino de ventanillas y el funcionario deje de ser un procesador de consultas mecánicas.
4.  Finalmente, CIVIA 360 no es una solución aislada; es una invitación a modernizar la administración pública local bajo un enfoque híbrido, donde la IA procesa el volumen y el humano recupera su rol de decisor estratégico y ético.

---

## 4. REFERENCIAS

Androutsopoulou, A., Karacapilidis, N., Loukis, E., & Charalabidis, Y. (2023). Transforming the communication between citizens and government through AI-guided chatbots. *Government Information Quarterly*, 36(2), 358–367.

Bright, J., Enock, F. E., Esnaashari, S., Francis, J., Hashem, Y., & Morgan, D. (2024). *Generative AI is already widespread in the public sector*. arXiv. https://doi.org/10.48550/arXiv.2404.13702

Brynjolfsson, E., Li, D., & Raymond, L. (2023). *Generative AI at Work*. National Bureau of Economic Research. https://www.nber.org/papers/w31161

City of Seattle (2025). *City of Seattle 2025-2026 AI Plan*. https://www.seattle.gov/

Galar Idoate, M. (s. f.). *Fundamentos de la inteligencia artificial generativa* [Presentación académica].

ICMA (2024). *Artificial Intelligence in Local Government: Survey Summary Report*. International City/County Management Association.

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *Advances in Neural Information Processing Systems*, 33, 9459–9474.

Li, X., Wang, Z., & Chen, Y. (2025). ARGUS: A Retrieval-Augmented QA System for Government Services. *Applied Sciences*, 15(4), 2187. https://doi.org/10.3390/app15042187

Management Solutions (2024). *El auge de los large language models: de los fundamentos a la aplicación*. https://www.managementsolutions.com/

National Institute of Standards and Technology (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1).

Nugroho, R., Pratama, A., & Wijaya, S. (2024). The Role of AI-Based Chatbots in Improving Public Services in Government Services in the Digital Era. *International Journal of Social Research*, 3(8), 2315–2326.

OECD.AI (2026). *AI in Government: Overview*. Policy Observatory.

Porter, Z., Khanna, R., Rawat, B., & Avis, N. (2024). Anthropomorphism and the social perception of AI assistants. *AI and Ethics*, 4(3), 805–818.

SAS & Coleman Parkes Research (2025). *Journey to GenAI Future: Strategic Path to Success in Government*. https://www.sas.com/

Universidad César Vallejo (2026). *Indicaciones para el desarrollo del primer avance del producto integrador colaborativo – Sesión 1*.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.

Vera, D. & Carrión, M. (2026). RAG-based chatbot for tax consultation services: A case study in Ecuador. *ResearchGate Preprint*.

Xu, Z. (2024). Hallucination is inevitable: An innate limitation of large language models. *arXiv*. https://doi.org/10.48550/arXiv.2401.11817

Zhou, J., Shen, R., You, Y., DiSalvo, C., Dombrowski, L., & MacLellan, C. (2025). Improving Public Service Chatbot Design and Civic Impact: Investigation of Citizens' Perceptions of a Metro City 311 Chatbot. *arXiv*.

---

## 5. ANEXOS

### Anexo 1. Árbol del problema (Génesis y efectos)

*   **El nudo central:** Ineficiencia sistémica y ausencia de una voz institucional coherente en la atención de trámites y reclamos municipales.
*   **Las raíces:** Fragmentación de la información (silos documentales), desactualización de las normas de cara al ciudadano y una dependencia absoluta de la memoria del personal para responder consultas que deberían ser automáticas.
*   **El impacto:** Frustración ciudadana, colas innecesarias y una pérdida de tiempo que se traduce en un descrédito de la gestión pública local.

### Anexo 2. El viaje del ciudadano con CIVIA 360

1.  **Consulta:** El vecino pregunta en lenguaje natural ("¿Qué necesito para renovar mi licencia?").
2.  **Búsqueda:** El motor RAG rastrea el TUPA y las ordenanzas vigentes en milisegundos.
3.  **Respuesta:** El sistema explica los pasos citando la fuente legal.
4.  **Triage:** Si el caso es complejo o requiere decisión administrativa, la IA genera un borrador y lo deriva a un funcionario para su validación final.

### Anexo 3. Gestión de riesgos en el despliegue

| Riesgo | Consecuencia | Nuestra salvaguarda |
| :--- | :--- | :--- |
| Alucinaciones | Datos falsos al vecino | Uso estricto de RAG (solo responde si está en el documento oficial). |
| Privacidad | Fuga de datos personales | Filtros de anonimización profunda antes de cualquier procesamiento. |
| Sesgos | Trato desigual en respuestas | Auditoría constante de los flujos de conversación y lenguaje inclusivo. |
| Desgobierno | Normas desfasadas | Designación de un curador de datos que verifique la vigencia de las fuentes. |
