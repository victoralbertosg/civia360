"""Root entry point for Streamlit Cloud.

Historically this repository contained a duplicate `app.py` at the project root.
That version attempted to load example files via ``add_documents(example_files)``
and raised an ``AttributeError`` because the objects in ``example_files`` are
``Path`` instances (they do not provide a `.read()` method).

The functional implementation now lives under `civia360/app.py` where the
loading logic has been corrected. To avoid the crash we provide a thin wrapper
that simply forwards execution to the real application.
"""

import streamlit as st
from pathlib import Path
import importlib.util

st.write("🔄 Redirecting to the main CIVIA 360 demo…")

# Dynamically load the real app module from the subdirectory.
app_path = Path(__file__).parent / "civia360" / "app.py"
spec = importlib.util.spec_from_file_location("civia360.app", app_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

st.success("✅ Application loaded successfully.")
