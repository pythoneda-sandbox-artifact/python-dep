---
type: Adapter
title: "LocalPythonDep"
description: "A locally-cloned PythonDep."
resource: https://github.com/pythoneda-sandbox-artifact/python-dep/blob/main/pythoneda/sandbox/dep/artifact/infrastructure/local_python_dep.py
tags: [infrastructure]
generated: { by: pythoneda-grill/deepseek-v4-pro, at: 2026-11-02T19:55:27Z }
sources:
  - id: src
    resource: https://github.com/pythoneda-sandbox-artifact/python-dep/blob/main/pythoneda/sandbox/dep/artifact/infrastructure/local_python_dep.py
    title: pythoneda/sandbox/dep/artifact/infrastructure/local_python_dep.py
  - id: readme
    resource: https://github.com/pythoneda-sandbox-artifact/python-dep/blob/main/README.md
    title: README.md
status: draft
---

A locally-cloned PythonDep.

Class name: LocalPythonDep

Responsibilities:
    - Represent the PythonDep artifact.

Collaborators:
    - pythoneda.shared.artifact.Artifact: Common logic for Artifacts.
    - pythoneda.sandbox.dep.artifact.application.PythonDepApplication: To initialize this class.
