# LOKA x AWS Immersion Day: SageMaker ala Carte

Code used in the AWS Immersion Day: SageMaker ala Carte organized by Loka and celebrated on November 2nd of 2021.

## Repo Structure

Repository mainly composed by:

- `training`
- `deployment`

## 1. Training an ML model

In order to show different capabilities of SageMaker when deploying ML models, 2 models were trained prior the event and artifacts were provided to attendants. All code and data related to model training can be found inside [training](training) folder.

```
IMPORTANT NOTE: Before trying the following notebooks, activate the conda environment included in this repo as follows:
```

```
conda env create -f environment.yml && conda activate aws-inmmersion
```

### Training a Model with SageMaker's XGBoost

To train a model using xtreme gradient boosting framework that SageMaker uses using SageMaker Python SDK we used the code inside [xgboost_customer_churn.ipynb](training/xgboost_customer_churn.ipynb) Jupyter notebook. This model is trained using SageMaker instances, therefore, expect a training job to be inititated and an `tar.gz` artifact to be stored in an S3 bucket in your AWS account.

```
IMPORTANT NOTE: For executing this one, you should create a proper AWS IAM role with enough permissions to access SageMaker and S3. Read the notebook for further details.
```

### Training a Model with Scikit Learn

To train a model using scikit-learn defacto Python ML library we used the code inside [scikitlearn_churn_prediction.py.ipynb](training/scikitlearn_churn_prediction.py.ipynb) Jupyter notebook. This notebook can be executed locally as long as the conda environment in this repo is activated or the Python environment used has `scikit-learn==0.24.2`.

```
IMPORTANT NOTE: scikit-learn version should be the same used in [deployment/requirements.txt](requirements.txt) otherwise, deployment will fail.
```

## 2. Deploying an ML model

This folder is composed by:

- [__`custom_container`__](deployment/custom_container/): Dockerfile, scripts and configuration files to create a Docker image that ships a scikit-learn model into Elastic Container Registry (ECR) for SageMaker to use when creating an endpoint.
- [__`local_notebook`__](deployment/local_notebook/): Notebook to deploy models locally using your `AWS CLI` credentials/profiles rather than using SageMaker notebooks/SageMaker Studio notebooks.
- [__`model`__](deployment/model/): XGBoost model artifact.
- [__`test_data`__](deployment/test_data/): Test and validation files to evaluate model performance and send requests to SageMaker endpoint.
- [__`sagemaker-inference-immersion-day-studio-ver-attendee`__](deployment/sagemaker-inference-immersion-day-studio-ver-attendee.ipynb): Version that is meant to be used by the attendees while following instructions given by expositors.
- [__`sagemaker-inference-immersion-day-studio-ver`__](deployment/sagemaker-inference-immersion-day-studio-ver.ipynb): Version with _full code_ and comments that is meant to be run as it is inside SageMaker Studio.

```
IMPORTANT NOTE: Workshop notebooks i.e. sagemaker-inference-immersion-day-studio-ver-attendee and sagemaker-inference-immersion-day-studio-ver are meant to be run inside **SageMaker Studio** otherwise, code will fail.
```