import xlrd


class Populator:
    def __init__(self, path: str, model, sheet=0):
        self.path = path
        self.model = model
        self.sheet = sheet

    def __str__(self):
        return str(self.model)

    def populator(self):
        work_book = xlrd.open_workbook(self.path)
        sheet = work_book.sheet_by_index(self.sheet)

        # extracting column names
        col_names = []
        for cell in sheet.row(0):
            col_names.append(cell.value)

        # going through all the rows with data except the first one
        for rownumber in range(sheet.nrows)[1:]:
            row = sheet.row_values(rownumber)
            entry = dict()  # accumulating data for one entry in dictionary
            # col iterator
            # index corresponds with col_name of a column value
            for index, col in enumerate(row):
                entry[col_names[index]] = col
            self.model.objects.create(**entry)
            
        return 'Populating is over'
