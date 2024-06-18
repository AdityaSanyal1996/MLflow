import os
import pandas as pd
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig




class DataValidation:
    def __init__(self, config : DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status = None

            #we want to erase the contents from the previous run
            with open(self.config.STATUS_FILE, 'w') as f:
                pass


            all_schema_types = []
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()
           # all_schema_types = self.config.all_schema.values()
            
            for element in self.config.all_schema.values():
                all_schema_types.append(str(element))
            #for validating the data types
            
            for col in all_cols:
                if str(data.dtypes[(col)]) not in all_schema_types: #not entering the if
                    validation_status = False
                    break
                    
                else:
                    validation_status = True

            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Type Validation status: {validation_status}")

                f.write("\n")
            
            #for validating the columns
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    break
                else:
                    validation_status = True
            
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Column Validation status: {validation_status}")
            

            

            return validation_status
        
        except Exception as e:
            raise e