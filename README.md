# Kedro TF Multimodal :hammer: [Template]

[![kedro-tf-text](https://github.com/dermatologist/kedro-multimodal/blob/develop/notes/multimodal.drawio.svg)](https://github.com/dermatologist/kedro-multimodal/blob/develop/notes/multimodal.drawio.svg)

This is a *template* for **multi-modal machine learning in healthcare** using the [Kedro](https://kedro.org/) framework. You can combine reports, tabular data and images using various fusion methods (Early & Late fusion. Few other fusion methods and graph data are WIP). This project works with [Kubeflow](https://www.kubeflow.org) and [Vertex AI](https://cloud.google.com/vertex-ai).

## Usage
* If you are not familiar with the [Kedro](https://kedro.org/) platform, please read the [overview](#overview) :point_down:
* This is a template repository. Generate a new repository with the same directory structure by clicking the **Use this template** button :point_up: and use it as a [Kedro project.](https://kedro.readthedocs.io/en/stable/get_started/new_project.html)
* Install dependenties ``` pip install -r src/requirements.lock ```
* Refer [default pipeline](src/kedro_tf_multimodal/pipelines/train/pipeline.py) for usage examples.
* Refer [sample data](/data/01_raw/) for data format. Prefix model datasets with appropriate model type from image_ , text_ , tabular_ , and bert_. (text_ is for CNN text models)
* Refer [catalogue](conf/base/catalog.yml) for inputs and outputs
* See [parameters](conf/base/parameters/train.yml) that can be tweaked.

The required pipelines are in [requirements.txt](src/requirements.txt). More details on the components are in their respective repositories :point_down: (PR welcome. Read CONTRIBUTING.md in the repositories)
* [kedro-tf-image](https://github.com/dermatologist/kedro-tf-image)
* [kedro-tf-text](https://github.com/dermatologist/kedro-tf-text)
* [kedro-tf-utils](https://github.com/dermatologist/kedro-tf-utils)
* [kedro-dicom](https://github.com/dermatologist/kedro-dicom) (*optional*) for processing DICOM images
* [kedro-graph](https://github.com/dermatologist/kedro-graph) (*optional*) for creating [DGL](https://www.dgl.ai/) graph from multimodal data.
* [fhiry](https://github.com/dermatologist/fhiry) (*optional*) for flattening [FHIR resources](https://www.hl7.org/fhir/overview.html).

## Features
* Use any number/combination of data types.
* Export trained fusion model for TF serving with an additional signatureDef for receiving image as b64 string. Use SERVING: path/to/save/model in [parameters](conf/base/parameters/train.yml). Also see [serving.py](serving.py) (example serving REST client) and [serving.sh](serving.sh) (start TF serving docker container with the model).
* Experimental support for **BERT** models with some [caveats.](#troubleshoot)

## You can visualize pipelines using [kedro-viz](https://github.com/kedro-org/kedro-viz). See the default pipeline below.
* Please note that you can build any multi-modal architecture!


[![kedro-viz](https://github.com/dermatologist/kedro-multimodal/blob/develop/notes/kedro-viz.png)](https://github.com/dermatologist/kedro-multimodal/blob/develop/notes/kedro-viz.png)

## Give us a star ⭐️
If you find this project useful, give us a star. It helps others discover the project.


## Troubleshoot
* Downloaded BERT models will not copy vocab.txt in assets folder to the newly created fusion model. This has to be manually copied.
* The class_num in TfModelWeights must be equal to to NCLASSES during training. Otherwise it throws an error:  Tensorflow estimator ValueError: logits and labels must have the same shape ((?, 1) vs (?,))
* *import tensorflow_text as text* is required in pipeline_registry to avoid this error: Op type not registered 'CaseFoldUTF8' in binary running on xxxx
* Inconsistent NCLASSES leads to **ValueError: `logits` and `labels` must have the same shape, received ((None, 3) vs (None, 1)).**

## Contributors

* [Bell Eapen](https://nuchange.ca) | [![Twitter Follow](https://img.shields.io/twitter/follow/beapen?style=social)](https://twitter.com/beapen)

## Overview

This is your new Kedro project, which was generated using `Kedro 0.18.4`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

## Project dependencies

To generate or update the dependency requirements for your project:

```
kedro build-reqs
```

This will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`. You can see the output of the resolution by opening `src/requirements.lock`.

After this, if you'd like to update your project requirements, please update `src/requirements.txt` and re-run `kedro build-reqs`.

[Further information about project dependencies](https://kedro.readthedocs.io/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, `catalog`, and `startup_error`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to convert notebook cells to nodes in a Kedro project
You can move notebook code over into a Kedro project structure using a mixture of [cell tagging](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#release-5-0-0) and Kedro CLI commands.

By adding the `node` tag to a cell and running the command below, the cell's source code will be copied over to a Python file within `src/<package_name>/nodes/`:

```
kedro jupyter convert <filepath_to_my_notebook>
```
> *Note:* The name of the Python file matches the name of the original notebook.

Alternatively, you may want to transform all your notebooks in one go. Run the following command to convert all notebook files found in the project root directory and under any of its sub-folders:

```
kedro jupyter convert --all
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html)
