import os
import pandas as pd
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(self, config : DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status = True #initially stays true

            #we want to erase the contents from the previous run
            with open(self.config.STATUS_FILE, 'w') as f:
                pass


            #all_schema_types = []
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema_keys = self.config.all_schema.keys()
            
            #for validating the data types
            size = len(all_schema_keys) # for iterating through all the columns in the dataset
            count = 0 # keeping a track of iteratiion through the dataset
            for col in all_cols:            
                count += 1
                for key in list(all_schema_keys):
                    if (col == key):
                        if (str(data.dtypes[col]) != (self.config.all_schema)[key]):
                            validation_status  = False
                            logger.info(f"{col} type in dataset doesn't match with {key} in schema")
                            break

                #if type doesn't match, the control will come outside(here!)

                if count == size: #we need to check for all the cols and keys at once
                    pass #since it is the end of iteration, validation_status will remain True if no 
                         #mismatch occurs, otherwise the validation_status will become false
                else:
                    continue


            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Type Validation status: {validation_status}")

                f.write("\n")
            
            validation_status = True
            #for validating the columns
            for col in all_cols:
                if col not in all_schema_keys:
                    validation_status = False
                    logger.info(f"{col} column doesn't match with schema")

            
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Column Validation status: {validation_status}")
            

            

            return validation_status
        
        except Exception as e:
            raise e