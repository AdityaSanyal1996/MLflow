from dataclasses import dataclass
from pathlib import Path

#for data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path

#for data validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE : str
    unzip_data_dir: Path
    all_schema: dict

#for data transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    data_path : Path