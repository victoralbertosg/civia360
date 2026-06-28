# INFORME TÉCNICO: EVALUACIÓN DE TECNOLOGÍAS Y MODELOS
## PROYECTO CIVIA 360

**Fecha:** 6 de junio de 2026  
**Dirigido a:** Equipo de Gestión del Proyecto CIVIA 360  
**Asunto:** Selección de ecosistema tecnológico para la optimización de la atención ciudadana municipal mediante IA Generativa.

---

### 1. Resumen Ejecutivo
El presente informe evalúa las herramientas y arquitecturas más idóneas para ejecutar la propuesta **CIVIA 360**. El objetivo central es garantizar un sistema que combine alta fidelidad en la recuperación de normatividad municipal (evitando alucinaciones), respeto estricto a la privacidad de datos personales y una escalabilidad que soporte la carga administrativa de una entidad de gobierno local.

### 2. Evaluación de Modelos de Lenguaje (LLM)

Para CIVIA 360, se han evaluado dos paradigmas de despliegue:

#### A. Modelos Propietarios (Frontera)
*   **Seleccionados:** **GPT-4o** y **Claude 3.5 Sonnet**.
*   **Desempeño:** Presentan el nivel más alto de razonamiento lógico y proficiencia en lenguaje administrativo español.
*   **Uso Ideal:** Fase de prototipado rápido y servicios de atención ciudadana que no involucren datos sensibles de alto riesgo.

#### B. Modelos de Código Abierto (Soberanía de Datos)
*   **Seleccionados:** **Llama 3.1 (70B)** y **Mistral Large 2**.
*   **Desempeño:** Altamente competitivos en tareas de resumen y extracción de datos. Su gran ventaja es la capacidad de ser desplegados en servidores locales (On-premise).
*   **Uso Ideal:** Procesamiento de expedientes internos, datos personales identificables y entornos donde la seguridad de la información es la prioridad máxima.

### 3. Stack Tecnológico de Recuperación (Arquitectura RAG)

La arquitectura de Generación Aumentada por Recuperación (RAG) es la columna vertebral del proyecto. Se recomiendan los siguientes componentes:

*   **Orquestador de Datos:** **LlamaIndex**. A diferencia de otros marcos, LlamaIndex está optimizado específicamente para indexar y consultar documentos estructurados complejos (como el TUPA o decretos municipales), ofreciendo una mejor gestión de contextos jerárquicos.
*   **Almacenamiento Vectorial:** 
    *   **Qdrant:** Seleccionado por su eficiencia en la nube y local, permite la búsqueda híbrida (semántica y por palabras clave), lo cual es crítico para encontrar artículos específicos por su número (ej. "Artículo 14").
    *   **pgvector:** Si la municipalidad ya utiliza infraestructura PostgreSQL, esta opción facilita el cumplimiento normativo al unificar la base de datos relacional con la vectorial.
*   **Modelo de Embeddings:** **Cohere Multilingual v3**. Este modelo es fundamental para capturar el significado del español administrativo peruano, diferenciando con precisión términos técnicos legales de los coloquiales.

### 4. Infraestructura y Seguridad

El despliegue de CIVIA 360 debe contemplar tres niveles de seguridad:

1.  **Gobernanza de Datos:** Implementación de técnicas de **anonimización** y **enmascaramiento de datos** (PII) antes de que cualquier información sea procesada por el modelo de lenguaje.
2.  **Soledad de Datos (Data Residency):** Se recomienda un entorno de **Nube Gubernamental (GovCloud)** o un nodo local que cumpla con la Ley de Protección de Datos Personales (Ley N° 29733).
3.  **Auditabilidad:** El sistema debe registrar una traza de auditoría de cada respuesta generada, citando explícitamente el documento y párrafo de origen mediante la técnica de "Grounding".

### 5. Hoja de Ruta de Implementación Sugerida

1.  **Fase 1 (Semanas 1-2):** Curaduría y digitalización vectorial de los documentos base (TUPA, Ordenanzas).
2.  **Fase 2 (Semanas 3-4):** Configuración del motor RAG con LlamaIndex y pruebas de estrés para detectar alucinaciones en temas críticos (multas, plazos).
3.  **Fase 3 (Semanas 5-6):** Integración de la capa de "Human-in-the-loop" para la supervisión de casos sensibles y despliegue del piloto en un área específica.

### 6. Recomendación Final del Equipo Técnico
Para un equilibrio óptimo entre costo, seguridad y rendimiento, se recomienda iniciar el proyecto con una arquitectura basada en **Llama 3.1 70B** (vía Azure Gov o servidor local) orquestada por **LlamaIndex** y **Qdrant**. Este ecosistema garantiza que la municipalidad mantenga el control absoluto de su información mientras ofrece un servicio de atención de vanguardia a sus ciudadanos.

---
**Elaborado por:** Departamento de Inteligencia Artificial  
**Proyecto:** CIVIA 360 - Transformación Digital Municipal
