# By Kian-RZ - Github: https://github.com/Kian-RZ
# Spliting The Text, Number And Symbols From Together With Object Oriented Programing
# 001 Practice Of Python Class

from colored import fore, style
import os

class Spliter:
    """
    A Class For My Program
    """
    def __init__(self,entry,status=True):
        self.a1, self.a2, self.a3 = [], [], []
        self.b1, self.b2, self.b3 = 0, 0, 0
        self.entry = entry
        self.all_texts = []
        self.status = status

    def result_print(self,char,kind):
        print(f"{fore('blue')}  -> {char} is {kind}{style('reset')}")

    def split_from_text(self):
        """
        Spliting The Text, Number And 
        Symbols From Together 
        """
        # Spliting Part

        special_characters = "\"!@#$%^&*()-+?_=,<>/\\"      # Symbols List
        all_chars = list(self.entry)
        print('\n')
        for char in all_chars:
            try:
                self.a2.append(int(char))
                kind = 'Number'
                self.result_print(char,kind)
            except:
                if char not in list(special_characters):
                    if char != ' ':
                        self.a1.append(char)
                        kind = 'Text'
                        self.result_print(char,kind)
                    self.all_texts.append(char)
                else:
                    self.a3.append(char)
                    kind = 'Special Character ( Symbol )'
                    self.result_print(char,kind)
        # Counting Part

        self.b1, self.b2, self.b3 = len(self.a1), len(self.a2), len(self.a3)
    
    def final_result(self):
        # Printing Final Result

        if self.status == True:
            print(f'{fore('green')}\n  -> Count Of Elements{style('reset')}')
            print(f'{fore('green')}\n  -> Text    ( Count Of Letters )  : {self.b1}{style('reset')}')
            print(f'{fore('green')}  -> Text    : {''.join(self.all_texts)}{style('reset')}')
            print(f'{fore('green')}  -> Number  : {self.b2}{style('reset')}')
            print(f'{fore('green')}  -> Symbol  : {self.b3}\n\n{style('reset')}')
        else:
            print(f'{fore('red')}  -> You Should First Have An Active Entry{style('reset')}')

    def symbol_detail(self):
        if self.status == True:
            print(f'{fore('green')}\n  -> Count Of Elements{style('reset')}')
            print(f'\n{fore('green')}  -> Symbol  : {self.b3}\n{style('reset')}')
        else:
            print(f'{fore('red')}   -> You Should First Have An Active Entry{style('reset')}')
    
    def text_detail(self):
        if self.status == True:
            print(f'{fore('green')}\n  -> Count Of Elements{style('reset')}')
            print(f'\n{fore('green')}\n  -> Text    ( Count Of Letters )  : {self.b1}{style('reset')}')
            print(f'{fore('green')}  -> Text    : {''.join(self.all_texts)}\n{style('reset')}')
        else:
            print(f'{fore('red')}  -> You Should First Have An Active Entry{style('reset')}')

    def number_detail(self):
        if self.status == True:
            print(f'\n{fore('green')}  -> Count Of Elements{style('reset')}')
            print(f'\n{fore('green')}  -> Number  : {self.b2}\n{style('reset')}')
        else:
            print(f'{fore('red')}  -> You Should First Have An Active Entry{style('reset')}')
    
    def entry_detail(self):
        if self.status == True:
            print(f'\n{fore('green')}  -> Entry: {self.entry}{style('reset')}')
        else:
            print(f'{fore('red')}  -> You Should First Have An Active Entry{style('reset')}\n')

    def change_entry(self,new_entry):
        self.entry = new_entry

class Exporter:
    """
    Exports A Result To File
    """
    def __init__(self,path=''):
        self.path = path

    def export(self,data):
        if self.path.strip(' ') != '':
            save_in = self.path + '\spliter_export.txt' if self.path[len(self.path)-1] != '\\' or self.path[len(self.path)-1] != '/' else self.path + 'spliter_export.txt'
            try:
                with open(save_in,'w+') as file:
                    file.write(data)
                    file.close()
            except:
                print(f'{fore('red')}  -> Error While Saving Report File{style('reset')}')
        else:
            print(f'{fore('red')}  -> You Should Add A Path With Command < path >{style('reset')}')
    
    def change_path(self,new_path):
        self.path = new_path


class InteractiveShell:
    """
    Interactive Shell For Be More Useable For Users
    """
    def __init__(self,spliter_class,exporter_class):
        self.spliter_class = spliter_class
        self.spliter = spliter_class('',status=False)
        self.exporter = exporter_class()
        print('\n')

    def execute(self,entry):
        self.spliter.change_entry(entry)
        self.spliter.status = True
        self.spliter.split_from_text()
        self.spliter.final_result()

    def clear_screen(self):
        try:
            os.system('cls')
        except:
            os.system('clear')

    def help_page(self):
        print(f'\n{style('bold')}   Command -- Work{style('reset')}')
        print(                 '   help    -> Help')
        print(                 '   run     -> Run The Spliting System')
        print(                 '   symbol  -> Current Symbols Detail')
        print(                 '   text    -> Current Texts Detail')
        print(                 '   number  -> Current Numbers Detail')
        print(                 '   detail  -> Current Details')
        print(                 '   entry  -> Current Details')
        print(                 '   clear   -> Clears Screen')
        print(                 '   cls     -> Clears Screen')
        print(                 '   export  -> Export Result')
        print(                 '   path    -> Add/Edit Path Of Export')
        print(                 '   about   -> About Me')
        print(                 '   exit    -> Exits From Program\n')

    def about_me(self):
        text = "   I Am Kian Rezaee, 7th Grade Of High School\n   Fullstack Web Developer And Python Programer\n   GitHub: https://github.com/Kian-RZ"
        print(f'{style('bold')}{text}{style('reset')}')

    def export(self):
        data = f'Entry -> {self.spliter.entry}\n\n'
        data += f'Count Of Elements\n Text    ( Count Of Letters )  : {self.spliter.b1}\n Text    : {''.join(self.spliter.all_texts)}\n Number  : {self.spliter.b2}\n Symbol  : {self.spliter.b3}\n'
        self.exporter.export(data)

    def shell(self):
        self.clear_screen()
        running = 1
        while running:
            command = input(f'{fore('yellow')} -> Enter Command ( Help With < help > Command ) :  {style('reset')}')
            if command == 'help':
                self.help_page()
            elif command == 'run':
                split_command = input(f'{fore('cyan')}  -> Enter You Value :  {style('reset')}')
                if split_command != 'exit':
                    if split_command.strip(' ') != '':
                        self.execute(split_command)
                    else:
                        print(f'{fore('red')}  -> Command Should Not Be Empty{style('reset')}')
            elif command == 'clear' or command == 'cls':
                self.clear_screen()
            elif command == 'exit':
                exit()
            elif command == 'symbol':
                self.spliter.symbol_detail()
            elif command == 'text':
                self.spliter.text_detail()
            elif command == 'detail':
                self.spliter.final_result()
            elif command == 'number':
                self.spliter.number_detail()
            elif command == 'about':
                self.about_me()
            elif command == 'path':
                export_command = input(f'{fore('cyan')}  -> Enter You Path :  {style('reset')}')
                if export_command != 'exit':
                    if export_command.split(' ') != '':
                        self.exporter.change_path(export_command)
                    else:
                        print(f'{fore('red')}  -> Path Should Not Be Empty{style('reset')}')
            elif command == 'export':
                self.export()
            elif command == 'entry':
                self.spliter.entry_detail()
            else:
                print(f'{fore('red')}  -> ERROR: You Command Is Invalid{style('reset')}')

if __name__ == '__main__':
    shell = InteractiveShell(Spliter,Exporter)
    shell.shell()