# Databricks notebook source
import os


# COMMAND ----------

notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
folder_path_ = os.path.dirname(notebook_path)
folder_path = f"/Workspace{folder_path_}"
# folder_path = f"{folder_path_}"

print(folder_path)

# COMMAND ----------

maz_stock_inventory_plus = dbutils.notebook.run(
        f"{folder_path}/test", 
        timeout_seconds=0
        # arguments={
        #     "mchb": mchb,
        #     "mard": mard,
        #     "mbew": mbew,
        #     "marc": marc,
        # }
    )

# COMMAND ----------

path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
print(path)
# /Workspace/brewdat-maz-maz-finance-internalcontrol-repo-adb/data_consumption/internal_control/test
