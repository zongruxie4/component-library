# Project Roadmap

CLAIMED is a framework designed to transform your code into reusable, composable
components that can run across diverse execution environments with built-in
scaling and fault tolerance.

---

## Central Project Objective

- **C3 Compiler**: Develop a unified system that transforms arbitrary code into standardized, reusable AI and data components.
- **Seamless Deployment**: Enable components to run across heterogeneous environments including Kubernetes, Docker, Slurm, LSF, and local or virtual setups.
- **Infrastructure Abstraction**: Automate packaging, dependency resolution, and environment isolation to ensure consistent execution.
- **Parallelization**: Facilitate grid-computing style workload distribution across available compute resources with minimal user intervention.
- **Composability**: Promote reuse of data engineering, data science, and AI pipelines through a flexible but opinionated component ecosystem.

---

## Progress to Date

- Established core architecture for reusable data engineering, data science, and AI components.
- Implemented initial component registry and composition logic for modular and reproducible pipelines.
- Integrated foundational runtime support for Docker- and Kubernetes-based execution.
- Developed early prototypes of the C3 Compiler, converting Python and Bash workflows into self-contained components.
- Set up continuous integration pipelines.
- Shifted primary focus to the C3 Compiler for seamless composition, scaling, and multi-platform execution (EU funded).
- Developed containerless execution framework to remove reliance on Docker while maintaining reproducibility (EU funded).

---

## Future Developments

- **Dependency Minimization**: Streamline runtime to remove heavy infrastructure dependencies, improving portability and security.
- **Scalable Execution Backends**: Expand native support for Kubernetes, Docker, Slurm, LSF, and local/virtual environments.
- **Enhanced Developer Experience**: Simplify component creation and sharing via CLI and SDK improvements.
- **Automated Testing**: Integrate full test coverage into CI/CD pipelines with a target of ≥80%.

---

## Upcoming Releases

### v0.8 (Q4 2025)

- Core C3 Compiler with initial composition and multi-platform execution.
- Basic containerless execution prototype.
- CLI enhancements and improved developer onboarding.

### v0.9 (Q1 2026)

- Full dependency minimization pass.
- Expanded publishing targets (MLX, PyPI, Conda).
- Integrated test harness with coverage reporting.

### v1.0 (Mid 2026)

- Stable C3 Compiler release.
- Full-scale containerless execution support.
- Robust component ecosystem ready for production-scale deployment.
- Achieve ≥80% test coverage and validated reproducibility across environments.

---

CLAIMED empowers developers and researchers to focus on **innovation**, while
abstracting away infrastructure complexity and enabling scalable, reproducible,
and composable AI workflows.
