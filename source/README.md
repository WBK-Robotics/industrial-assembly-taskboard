# Source Files for Documentation

This folder contains the source files used to generate the documentation website for the Industrial Assembly Task Board. The documentation is built using [Sphinx](https://www.sphinx-doc.org/), a powerful documentation generator that converts these reStructuredText files into HTML, PDF, and other formats.

## Purpose

The source files in this folder define the structure and content of the documentation, including:

- Assembly instructions for building the task board and its modules.
- Task descriptions, objectives, and success criteria for benchmarking robotic systems.
- Overviews and guides to help users get started with the task board.

## Contributing

If you are contributing new tasks to the task board, please ensure that the documentation is updated accordingly. This includes:

1. Adding a new `.rst` file for the task description, objectives, and success criteria.
2. Updating the relevant index files to include links to the new task.
3. Ensuring that the new content is consistent with the existing documentation structure and style.

## Building the Documentation

To build the documentation locally:

1. Install Sphinx by following the [official installation guide](https://www.sphinx-doc.org/en/master/usage/installation.html).
2. Navigate to the root directory of this repository.
3. Run the following command to generate the HTML documentation:

   ```bash
   make html
   ```

4. The generated HTML files will be available in the `build/html` folder.

For more details on using Sphinx, refer to the [Sphinx documentation](https://www.sphinx-doc.org/).