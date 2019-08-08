import os
from datetime import datetime
from mysite.jxl import FILE_PATH

import xlwt as excel


class CreateExcelFile:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.book = excel.Workbook()
        self.filename = kwargs.get('filename')
        self.sheetname = kwargs.get('sheetname')

        self.sheet = self.book.add_sheet(self.sheetname or 'Sheet 1')

        print('Workbook initialized...')

    def __call__(self, *args, **kwargs):
        self.args = args
        self.filename = kwargs.get('filename')
        self.sheetname = kwargs.get('sheetname')
        self.sheet = self.book.add_sheet(self.sheetname or 'Sheet 1')

        print(f'Workbook filename and sheetname redefined as: filename={self.filename}, sheetname={self.sheetname}')

    def __repr__(self):
        return f'<CreateExcelFile Object: filename={self.filename}, sheetname={self.sheetname}">'

    def create_excel_book(self, data_list):
        print('Generating report...')
        self.write_data(data_list=data_list)
        self.save_and_close()

    def write_data(self, data_list):
        keys = []
        for i, dict_item in enumerate(data_list):
            for colx, (key, val) in enumerate(dict_item.items()):
                if key not in keys:
                    self.sheet.write(0, colx * 2, key)
                keys.append(key)
                self.sheet.write(i + 1 * 2, colx * 2, val)

    def save_and_close(self):
        filename = f'{self.filename}_{datetime.today().strftime("%Y_%m_%dT%H.%M.%S")}.xls'
        self.book.save(os.path.join(FILE_PATH, filename))
        print(f'Report finished. Excel file saved as "{filename}"')

    @staticmethod
    def get_recent_file():
        import glob
        assets = os.path.join(FILE_PATH, '*.xls')
        list_of_files = glob.glob(assets)
        latest_file = max(list_of_files, key=os.path.getctime)
        return os.path.basename(latest_file)
