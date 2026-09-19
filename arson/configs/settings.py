from pathlib import Path

class project_dir():

    CURRENT_DIR = Path(__file__).parent.parent.absolute()

    DATA_DIR = CURRENT_DIR/'home-risk-kaggle/data'

    RAW_DIR = DATA_DIR/'raw'

    PROCESSED_DIR = DATA_DIR/'processed'

    
