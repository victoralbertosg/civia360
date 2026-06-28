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

### 1. INTRODUCCIÓN

#### El problema en contexto y su trascendencia
Durante el diagnóstico de la gestión municipal contemporánea, se detectó un patrón crítico de ineficiencia en el tratamiento de reclamos y la orientación al administrado. Esta situación no fue aislada; por el contrario, surgió de la fragmentación documental y de una evidente demora en los tiempos de respuesta institucional. En la práctica, esto significó que un ciudadano en busca de trámites tan habituales como la obtención de una licencia municipal se enfrentara a criterios contradictorios, supeditados muchas veces a la interpretación subjetiva del servidor de turno.

Se determinó que el núcleo del problema organizacional radicó en la carencia de procesos estandarizados. A nivel interno, esto derivó en una sobrecarga laboral desproporcionada y una dificultad manifiesta para extraer datos útiles de las consultas ciudadanas. Desde la óptica del usuario, el impacto fue directo: frustración y una creciente desconfianza hacia el aparato estatal local. Resultó imperativo, por tanto, explorar soluciones tecnológicas que, como sugiere Bright et al. (2024), permitan aliviar la densidad burocrática mediante el uso estratégico de la Inteligencia Artificial Generativa (GenAI), siempre bajo un esquema de rigurosa gobernanza humana.

#### Fundamentación Teórica
Para comprender el alcance de la propuesta, es preciso delimitar qué entendimos por Inteligencia Artificial: un ecosistema computacional enfocado en el desarrollo de capacidades cognitivas sintéticas. En este marco, la vertiente Generativa (GenAI) se desmarcó de los sistemas tradicionales al no limitarse a la clasificación de datos, sino al ser capaz de proyectar contenido inédito mediante patrones profundos.

La trayectoria de esta tecnología no fue lineal. Pasamos de una lógica de reglas estáticas hacia paradigmas de aprendizaje profundo, alcanzando el estado del arte con los Modelos de Lenguaje de Extensa Escala (LLM). Lo que verdaderamente cambió las reglas del juego fue la arquitectura **Transformer**. Gracias al mecanismo de **autoatención**, estos modelos lograron "entender" —en términos estadísticos— la jerarquía de importancia de cada palabra en un párrafo, capturando matices del lenguaje natural que antes resultaban indescifrables para las máquinas (Vaswani et al., 2017).

En el plano de las organizaciones públicas, si bien los LLM actuaron como "copilotos" de alta eficiencia, no se ignoraron sus puntos ciegos. Nos referimos puntualmente a las "alucinaciones" y al denominado "Efecto Eliza", esa propensión de los usuarios a proyectar rasgos humanos en la IA, lo que podría nublar el juicio crítico. Por este motivo, la arquitectura propuesta para CIVIA 360 optó por el enfoque de **Generación Aumentada por Recuperación (RAG)**. A diferencia de un modelo libre, el RAG obligó al sistema a "leer" documentos de fuentes oficiales (TUPA, ordenanzas) antes de emitir cualquier respuesta, anclando la fluidez del lenguaje a la veracidad institucional (Lewis et al., 2020).

#### Horizonte de trabajo
El propósito central de este informe fue estructurar el proyecto **CIVIA 360**, concebido como una plataforma de soporte organizacional que emplee GenAI para revitalizar la atención ciudadana. A través de este análisis, se buscó no solo diagnosticar las causas de la ineficiencia municipal, sino fundamentar cómo el uso ético y técnico de la IA puede fortalecer la toma de decisiones basada en evidencia.

---

### 2. DESARROLLO

#### Exploración de las dimensiones del problema
La crisis de atención ciudadana no respondió a un factor único, sino a una convergencia de carencias documentales. La información solía estar "secuestrada" en archivos físicos desactualizados o en el conocimiento no documentado de los trabajadores más antiguos.

*   **Impacto en la Organización:** Se observó una dependencia excesiva del factor humano individual, lo que impidió a las jefaturas tomar decisiones estratégicas basadas en métricas de satisfacción reales.
*   **Impacto Social:** La asimetría informativa se convirtió en una barrera de acceso. Cuando un ciudadano no recibe información clara, el servicio público falla en su misión democratizadora.
*   **Dimensión Económica:** La eficiencia es, ante todo, un tema de costos. Se estimó que la implementación de asistentes IA puede optimizar entre el 27% y el 74% de la jornada administrativa dedicada a tareas repetitivas.
*   **Legitimidad Política:** La imagen de una municipalidad se construye en la ventanilla. Una respuesta tardía o errática proyecta una institución obsoleta; una respuesta ágil, en cambio, refuerza el contrato social.

#### Sinergia entre la Gestión Municipal y la GenAI
CIVIA 360 se diseñó no como un reemplazo, sino como un sistema de asistencia híbrida. Su estructura técnica descansó en la interconexión de tres componentes: un motor de lenguaje avanzado, una base de conocimiento vectorial anclada al TUPA y un protocolo de validación humana.

Entre las funcionalidades que se proyectaron destacan:
1.  **Orientación Interactiva:** Un canal capaz de resolver dudas complejas en tiempo real, citando la base legal correspondiente.
2.  **Soporte al Operador:** Herramienta para que el servidor público genere borradores de respuestas administrativas con mayor celeridad.
3.  **Filtrado Inteligente de Casos:** Capacidad para discriminar reclamos urgentes de consultas informativas, optimizando la ruta del expediente.
4.  **Minería de Datos Gerencial:** Generación de resúmenes semanales sobre los nudos críticos en la atención, permitiendo a los directivos ajustar estrategias de gestión sobre la marcha.

Es relevante subrayar que la implementación no fue ingenua. Consideramos los hallazgos de Brynjolfsson et al. (2023), quienes evidenciaron una mejora del 15% en la productividad operativa, pero también fuimos conscientes de los desafíos en privacidad de datos. Por ello, la propuesta se alineó con los estándares del **AI Act** de la UE, garantizando que el tratamiento de la información ciudadana sea transparente y seguro.

---

### 3. CONCLUSIONES

1.  Se comprobó que el obstáculo principal de la gestión local fue la dispersión del conocimiento y la ausencia de una interfaz ágil de orientación ciudadana.
2.  La Inteligencia Artificial Generativa se perfiló como la tecnología idónea para cerrar esta brecha, permitiendo la síntesis de información oficial en respuestas claras y accionables.
3.  El modelo RAG se estableció como la salvaguarda técnica necesaria para asegurar que la automatización sirva al interés público sin caer en errores de consistencia documental.
4.  Finalmente, CIVIA 360 representó una oportunidad para modernizar la administración pública local, transformando los reclamos en datos de valor y la atención en una experiencia de calidad para el vecino.

---

### 4. REFERENCIAS

Bright, J., Enock, F. E., Esnaashari, S., Francis, J., Hashem, Y., & Morgan, D. (2024). *Generative AI is already widespread in the public sector*. arXiv. https://doi.org/10.48550/arXiv.2404.13702

Brynjolfsson, E., Li, D., & Raymond, L. (2023). *Generative AI at Work*. National Bureau of Economic Research. https://www.nber.org/papers/w31161

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems.

Management Solutions (2024). *El auge de los large language models: de los fundamentos a la aplicación*. https://www.managementsolutions.com/

National Institute of Standards and Technology (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1).

OECD.AI (2026). *AI in Government: Overview*. Policy Observatory.

Universidad César Vallejo (2026). *Indicaciones para el desarrollo del primer avance del producto integrador colaborativo – Sesión 1*.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). *Attention is all you need*. Advances in Neural Information Processing Systems.

Zhou, J., Shen, R., You, Y., DiSalvo, C., Dombrowski, L., & MacLellan, C. (2025). *Improving Public Service Chatbot Design and Civic Impact: Investigation of Citizens’ Perceptions of a Metro City 311 Chatbot*. arXiv.

---

### 5. ANEXOS

**Anexo 1: Dashboard del Problema**
*   **Origen del conflicto:** Desactualización informativa y silos departamentales.
*   **Resultados nocivos:** Pérdida de legitimidad y estancamiento procesal.

**Anexo 2: Protocolo de Seguridad y Ética en CIVIA 360**

| Ámbito de Riesgo | Estrategia de Mitigación | Objetivo de Control |
| :--- | :--- | :--- |
| Alucinaciones Técnicas | Arquitectura RAG de fuente cerrada | Garantizar veracidad documental |
| Sesgos y Equidad | Entrenamiento con guías de lenguaje inclusivo | Evitar discriminación algorítmica |
| Soberanía de Datos | Cumplimiento estricto del AI Act | Proteger la privacidad del vecino |
| Dependencia Cognitiva | Auditorías de supervisión humana | Mantener autonomía del servidor |
