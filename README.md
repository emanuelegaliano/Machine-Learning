# ![Machine Learning Logo](readme_logo.png)

# Machine Learning Notes & Projects

This repository contains a comprehensive set of **Machine Learning lecture notes**, written in LaTeX, together with supporting code, figures, and project reports.

The material is designed to be rigorous, mathematically grounded, and suitable for university-level study.

---

# 📘 Main Notes

The core of this repository is the LaTeX manuscript:

```
Machine Learning.tex
```

which compiles into:

```
Machine Learning.pdf
```

The notes cover the theoretical and practical foundations of Machine Learning, including:

* Introduction to Machine Learning
* Linear Models
* Regression
* Classification
* Model Evaluation
* Neural Networks
* Decision Trees
* Random Forests
* Support Vector Machines
* Ensemble Learning
* Theoretical Insights and Seminar Extensions

All chapters are organized in the `chapters/` directory  and structured modularly for clarity and maintainability.

The document aims to:

* Provide formal derivations and mathematical rigor
* Connect theory and implementation
* Include illustrative figures and diagrams
* Offer intuitive explanations alongside proofs
* Present complete worked examples

---

# 📂 Repository Structure

Below is the logical organization of the repository :

## `chapters/`

Contains all main LaTeX chapter sources.

## `frontmatter/`

Contains front matter material (e.g., license page).

## `projects/`

Contains LaTeX source files for project reports.

## `codes/`

Python scripts and experimental code supporting the notes.

Example:

* `adaboost_decision_boundary.py`

## `drawings/`

Vector drawings (.drawio) used to generate high-quality diagrams.

## `images/`

All figures used in the notes (plots, diagrams, illustrations, schemas).

## `refs.bib`

Bibliographic references used throughout the manuscript.

## `out/`

Compilation output directory (ignored via `.gitignore`).

---

# 🧪 Projects

This section contains projects developed and discussed in the notes.

Each project is written in LaTeX and included in the final compiled PDF.

## Template for Future Projects

### Project Title

**Description:**
Brief description of the problem addressed.

**Objective:**
Explain the learning task (classification, regression, etc.).

**Methods Used:**
List of algorithms, models, or techniques applied.

**Results:**
Summary of experimental findings.

**Files:**

* `projects/project-name.tex`
* Associated datasets (if any)
* Supporting scripts (if any)

---

(Currently included projects are located in the `projects/` directory.)

---

# 🛠 How to Compile

The project uses a `Makefile` to manage compilation.

All auxiliary files are generated inside the `out/` directory, and the final PDF is copied to the root of the repository.

## Compile the Document

From the root of the repository, run:

```bash
make
```

This will:

* Compile the document using `latexmk`
* Automatically run BibTeX if required
* Store all intermediate files (`.aux`, `.log`, `.toc`, etc.) inside `out/`
* Copy the final `Machine Learning.pdf` to the repository root

## Clean Build Files

To remove all generated auxiliary files:

```bash
make clean
```

## Requirements

* A LaTeX distribution (TeX Live, MiKTeX, etc.)
* `latexmk`
* `bibtex`

---

# 🤝 Contributing

Contributions are very welcome.

You can contribute by:

* Opening **issues** (typos, conceptual mistakes, improvements)
* Submitting **pull requests**

## Pull Request Requirements

If you submit a pull request, please ensure that:

1. ✅ You modify the **LaTeX source files**, not only the PDF
2. ✅ You confirm that the project compiles successfully using method in section above
3. ✅ You upload the newly compiled `Machine Learning.pdf`
4. ❗ You do **not** modify the repository structure unless strictly necessary
5. ❗ You do **not** change the used libraries in Machine Learning.tex unless necessary
6. ✅ You add your name to the *Contributors* section at the end of this README

Pull requests that do not meet these requirements may not be accepted.

---

# 👨‍🏫 Authors

* **[Emanuele Galiano](https://github.com/emanuelegaliano)**
* **[Damiano Trovato](https://github.com/BoredDam)**

---

# 🙌 Contributors

* **[Paolo Volpini](https://github.com/paolovolpini)**
  Added notes on the MLP case study.

* **[Diego Martinez](https://github.com/Diego54523)**
  Reported errors in issues #1, #2, and #3.

---

# 📜 License

See `frontmatter/license.tex` for license details.