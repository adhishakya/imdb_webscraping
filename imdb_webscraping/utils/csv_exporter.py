import os
from scrapy.exporters import CsvItemExporter

class CustomCsvItemExporter(CsvItemExporter):
    def __init__(self, file, **kwargs):
        self.file = file
        file_exists = os.path.exists(file.name) and os.path.getsize(file.name) > 0 # checking file existence and if it has content
        kwargs['include_headers_line'] = not file_exists  # dont include headers if file exists and is not empty else include headers
        super().__init__(file, **kwargs) # calling the CsvItemExporter constructor with the new kwargs
