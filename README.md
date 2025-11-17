# Electric-vehicle-
Electric Vehicle Range Prediction - Regression Analysis

# Project overview

This project focuses on predicting the driving range of electric vehicles (EVs) using regression-based machine learning models applied to a tabular dataset of EV characteristics and usage conditions.
Accurately estimating the remaining range on a single charge helps reduce driver anxiety, improves trip planning, and supports better charging decisions.

The analysis is implemented entirely in Jupyter Notebook(s), making it easy to explore the data, experiment with models, and visualize performance interactively.
The notebook walks through data preprocessing, feature engineering, model training, and evaluation using standard regression metrics.

# Problem statement

Electric vehicle range is the distance an EV can travel on its current battery charge, and it depends on many factors such as battery capacity, vehicle specifications, driving style, and environmental conditions.
The goal of this project is to build a regression model that can estimate the expected range given a set of input features describing the vehicle and driving scenario.

By learning the relationship between input variables and range, the model can be used as a decision-support tool for drivers, manufacturers, or charging infrastructure planners.

# Objectives

- Understand and prepare an EV-related dataset for range prediction (cleaning, handling missing values, and basic feature engineering).
- Explore the data with visualizations to identify key patterns and relationships that influence range.
- Train and compare regression models to predict the vehicle range from the available features.
- Evaluate models using common regression metrics and interpret which features have the strongest impact on range.

# Dataset description.

The project is designed to work with a structured dataset where each row represents a vehicle or a trip instance and columns describe technical and usage-related attributes.
Typical features may include battery capacity, energy consumption, vehicle weight or class, speed-related variables, and other operational parameters relevant to range.

You can adapt the notebook to any compatible EV dataset with numeric or categorical columns that are meaningful for range prediction.
Public EV range datasets with similar structure are often used in research and competitions, and the same preprocessing logic can be applied here.

# Methods and models.

The workflow follows a standard supervised learning pipeline for regression.
Key steps include splitting the data into training and test sets, scaling or encoding features where necessary, and fitting one or more regression models.

You can experiment with models such as linear regression, tree-based methods, or gradient-boosted regressors depending on dataset size and complexity.
Model performance is assessed using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and the coefficient of determination .

# Repository contents (suggested)

You can structure the repository in a simple, notebook-centered way so that others can quickly understand and run your work.

- `notebooks/` – Jupyter notebook(s) containing data exploration, preprocessing, model training, and evaluation steps.
- `data/` – Folder where you place raw and processed dataset files (often excluded from version control if large or private).
- `models/` – Optional directory to store saved models, predictions, or evaluation outputs for later reuse.
- `README.md` – Project documentation file describing the aim, methods, and how to run the notebook.

If your existing structure is different, you can keep the same section and just update the folder and file names to match your repository.

# How to run the notebook.

1. Clone the repository to your local machine using Git so you can run and modify the notebook.
2. Create a Python environment and install the typical data-science stack (for example: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, and `seaborn`).
3. Place your EV dataset file(s) in the `data/` directory or update the notebook path to point to your own data location.
4. Open the Jupyter Notebook in your preferred environment (Jupyter Lab, classic Jupyter, or VS Code) and run the cells in order from top to bottom.

If you use Google Colab, you can upload the notebook there and either upload the dataset manually or mount cloud storage to access it.

# Evaluation and metrics

To measure how well the model predicts range, the notebook uses standard regression metrics.
MAE gives an average absolute error in the same units as range, MSE penalizes larger errors more strongly, and $$R^2$$ indicates how much variance in range is explained by the model.

These metrics help you compare different models and configurations in a consistent way.
You can log or tabulate these scores to track improvements as you refine preprocessing steps or tune hyperparameters.

# Possible extensions

- Try additional algorithms such as ensemble methods or regularized regression to see if they improve accuracy or robustness.
- Perform more advanced feature engineering, including interaction terms or domain-specific transformations based on EV physics and energy consumption.
- Incorporate cross-validation and systematic hyperparameter tuning for a more reliable estimate of model performance.
- Extend the notebook to support scenario analysis (for example, simulating changes in speed or temperature and observing the predicted effect on range).

# How to use this project

This project can serve as a starting point for academic coursework, experiments on EV range prediction, or prototypes for dashboard and application backends.
You can fork the repository, adapt the notebook to your own dataset, and document any changes directly in markdown cells inside the notebook and in this README.

Remember to update this README with your exact dataset name, notebook filename, and any specific models or results once your analysis is finalized.

[1](https://github.com/Srivardhan-k/Electric-vehicle-)
[2](https://core.ac.uk/download/pdf/570969280.pdf)
[3](https://www.kaggle.com/code/cindynz/electric-vehicle-range-prediction)
[4](https://www.scribd.com/document/655000243/Electric-Vehicle-Range-Prediction-Regression-Analysis)
[5](https://github.com/srivardhan825)
[6](https://pmc.ncbi.nlm.nih.gov/articles/PMC11362498/)
[7](https://ijsrem.com/volume-09-issue-10-october-2025/)
[8](https://saranathan.ac.in/IQAC/AQAR2023/C6_5_3_iii_expert.pdf)
[9](https://www.kscst.org.in/spp/47_series/08_47S_SPP_sanctioned_projects_30July2024_with_NEFT_Transaction_Details.pdf)
[10](https://in.linkedin.com/in/shrivardhan-patil-a94609213)
[11](https://www.sciencedirect.com/journal/next-research/vol/2/issue/2)
[12](https://github.com/anushuk/Electric-vehicle-battery-range-prediction)
[13](https://www.bits-pilani.ac.in/wp-content/uploads/Part-1-PS-I-2024-Chronicles.pdf)
[14](https://sdmcet.ac.in/downloads/2023%20Data/Admindata/Final%20Mandatory%20Disclosure%20-%2003.10.2023.pdf?_t=1696327151)
[15](https://www.kaggle.com/code/prajwalmpoojary/predicting-ev-range-using-linear-regression)
[16](https://webthesis.biblio.polito.it/30272/1/tesi.pdf)
