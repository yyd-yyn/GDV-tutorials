# GDV

This repository contains exercises for the course "Grafische Datenverarbeitung" at HS Furtwangen University. Please note
that all content here is tentative and will be adapted to the student's needs during the semester.

## Forking the repository

To work on the exercises, you need to fork this repository to your GitHub account and clone it to your local machine. You can find a guide on how to do
this [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo). It is recommended to configure git to sync your forked repository with the original one as explained in the [guide further down the page](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#configuring-git-to-sync-your-fork-with-the-upstream-repository).

## Prerequisites

First, we need to download and install Python 3 from [python.org](https://www.python.org/downloads/). The recommended
version is `3.10.7` or above. Then, we can use the following terminal command to inspect the currently installed
version:
<table>
<tr>
<th>
Windows
</th>
<th>
MacOS
</th>
</tr>

<tr>

<td>
<pre>
python --version
</pre>
</td>

<td>
<pre>
python3 --version
</pre>
</td>

</tr>
</table>


*Ensure that the terminal and selected interpreter use the correct version.*

---

Usually, the Python installation includes the dependency management tool pip out of the box. If not, download and
install it from [pip.pypa.io](https://pip.pypa.io/en/stable/installation/). The minimum required version is `19.3` and
above. We can again use a terminal command to check the version:

<table>
<tr>
<th>
Windows
</th>
<th>
MacOS
</th>
</tr>

<tr>

<td>
<pre>
pip --version
</pre>
</td>

<td>
<pre>
python3 -m pip --version
</pre>
</td>

</tr>
</table>


If you need to update your pip version use 

```shell
python -m pip install --upgrade pip
```

*You might need to use ```python3``` instead of ```python``` on MacOS.*

## Getting Started with Python

A great selection of useful resources are:

- [https://www.python.org/about/gettingstarted/](https://www.python.org/about/gettingstarted/)
- [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- [https://code.visualstudio.com/docs/python/python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

## Setting up the development environment

Generally, one can use any code editor or IDE to follow these exercises, but we recommend that students use VS Code. You
can download VS Code from [https://code.visualstudio.com/][vsc-website]. On Linux, you can follow the instructions on
[this][vsc-linux] page. On Arch-based systems, you can use the OSS version `code` ([Link][vsc-arch-oss]) or the fully
featured proprietary version `visual-studio-code-bin` ([Link][vsc-arch-bin]) from AUR.

### VS Code extensions

- Python `ms-python.python`: Python support in VS Code ([Link][vsc-ext-python])
- Pylance `ms-python.vscode-pylance`: Python language server ([Link][vsc-ext-pylance])
- Python Image Preview `076923.python-image-preview`: you can quickly check your Python image data during debugging
  ([Link][vsc-ext-img-preview])
- Todo Tree `Gruntfuggly.todo-tree`: provides an overview of all code lines marked with "TODO"
  ([Link][vsc-ext-todo-tree])

### Python Virtual Environments

To more easily develop Python code, it is recommended to set up a virtual environment (VENV) in the project root folder.
The following terminal command will create the hidden folder `.venv` in your current project folder:

```shell
python -m venv .venv
```

*Do not forget to use ```python3``` instead of ```python``` on MacOS.*

Next, we need to enable the VENV. The VENV will only be active for the current terminal session. Closing the terminal and re-opening it will disable the VENV. So always make sure to enable it before you start developing.

```shell
# For Windows use
.venv\Scripts\Activate.ps1

# For Linux and Mac OS
source .venv/bin/activate
```

Special care is needed when using Windows. Please consult the following [guide][venv-guide] for more information. When the environment is activated, you should see this as a prefix on your terminal.

---

On both Operation Systems, one can deactivate the VENV with the following terminal command:

```shell
deactivate
```

### Installing dependencies

Installing the required dependencies is straightforward:

```shell
pip install .
```

This will load the defined dependencies in `pyproject.toml` and install them inside the VENV. Note that the ultralytics module needed for the last tutorials is excluded, as this sums up to more than one Gigabyte of data as some machine learning modules are included (e.g. torch).

If you want to install it later use:

```shell
pip install ultralytics
```

## Happy coding!

Now you are ready to start working on the exercises. The `tutorials/src` folder contains all the code. The idea is to start with the
`<XX>-<NAME>.problem.py` files and try to fulfill the TODOs. These "problem" files will guide you in the right
direction. You can ask for help during the lecture if there are any questions. Next, the `<XX>-<NAME>.solution.py` files
contain the solution. After you implement your solution, use this file to compare and add some improvements to your
code.

## Helpful resources

### Python

You can use https://docs.python.org/3/ as a starting point, and the [Library Reference][py-lib-ref] or the
[Language Reference][py-lang-ref] should contain all the needed information.

### OpenCV reference

See [https://docs.opencv.org/4.x/](https://docs.opencv.org/4.x/) for the OpenCV code reference. Here, all OpenCV methods are explained. If you want to know about parameters and flags, this is the page to look them up.

### NumPy

OpenCV uses NumPy `ndarrays` as the default format for data exchange. It can create, operate on, and work with NumPy
arrays. For some operations, import the NumPy module and use special functions provided by NumPy. Other libraries like
TensorFlow and SciPy also use NumPy. See the official [docs][numpy-docs] for the API reference.

[venv-guide]: https://docs.python.org/3/library/venv.html
[py-lib-ref]: https://docs.python.org/3/library/index.html
[py-lang-ref]: https://docs.python.org/3/reference/index.html
[numpy-docs]: https://numpy.org/doc/stable/reference/index.html

[vsc-ext-python]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[vsc-ext-pylance]: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
[vsc-ext-img-preview]: https://marketplace.visualstudio.com/items?itemName=076923.python-image-preview
[vsc-ext-todo-tree]: https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree

[vsc-website]: https://code.visualstudio.com/
[vsc-linux]: https://code.visualstudio.com/docs/setup/linux
[vsc-arch-oss]: https://archlinux.org/packages/community/x86_64/code/
[vsc-arch-bin]: https://aur.archlinux.org/packages/visual-studio-code-bin
