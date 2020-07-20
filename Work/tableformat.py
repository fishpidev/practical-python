class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a talbe in plain text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
       
    def headings(self, headings):
        begingHTML = '<tr>'
        endHTML = '</tr>'
        for h in headings:
            begingHTML += f'<th>{h}</th>'
        begingHTML += endHTML
        print(begingHTML)

    def row(self, rowdata):
        starttd = '<tr>'
        endtd = '</tr>'
        for d in rowdata:
            starttd += f'<td>{d}</td>'
        starttd += endtd
        print(starttd)
          
