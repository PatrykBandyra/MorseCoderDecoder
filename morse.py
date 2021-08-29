import tkinter as tk
from tkinter import scrolledtext, filedialog
import sys
from morse_coder_decoder import code, code_gui, decode, decode_gui


def display_help(help_button, root):
    help_window = tk.Toplevel()
    help_window.title('Help')
    help_window.geometry('1000x400')
    help_window.config(background='black')
    help = f'This is morse coder/decoder program.\nIt can be run as a graphical user interface or as a command '\
           f'line script.\nGraphical user interface instructions:\n1. Write text in upper text box - supported signs: '\
           f'all English alphabet letters, ".", ",", "?".\n2. Press "ENCODE" button to encode text to morse. Morse '\
           f'code will be displayed in lower text box.\n3. Press "EXPORT TO FILE" button to save the text or morse '\
           f'code to a file.\n4. Write morse code in lower text box - rules: each letter must be separated by a '\
           f'"space, \neach word must be separated by "space" and "/"; EXAMPLE: "I like sun" = ".. / .-.. .. -.- . / '\
           f'... ..- -."\n5. Press "DECODE" button to decode morse code. Text will be displayed in upper text box.\n'\
           f'Script rules:\n1. Script run in command line can only encode/decode text files.\n2. First write '\
           f'"Python morse.py " then specify argument: "encode" or "decode", next after a space: "t"/"terminal"\n'\
           f'to display encoded/decoded text in terminal or "f"/"file" to save encoded/decoded text to a file,\nthen '\
           f'after another space write input file path or input file name (with extension) if a file is in a '\
           f'directory in which script is running.\n3. If "file" option has been chosen, then you will be asked to ' \
           f'enter output file name.\nOutput file will be saved in a directory in which script is running.'
    label = tk.Label(help_window, text=help, font=('Arial', 12, 'normal'), bg='black', fg='red', anchor='nw')
    label.pack()


def export_to_file(text_box):
    filename = filedialog.asksaveasfilename(filetypes=[('Text file', '*.txt')], defaultextension='*.txt')
    if filename:
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(text_box.get(1.0, 'end'))


def main():
    root = tk.Tk()
    root.title('Morse coder/decoder')
    root.geometry('400x400')
    root.config(background='black')

    # HELP button
    help_button = tk.Button(root, text="HELP", fg='red', bg='black', font=('Arial', 8, 'bold'),
                            command=lambda: display_help(help_button, root))
    help_button.grid(row=2, column=0, pady=(5, 5))

    # FRAME1 ----------------------------------------------------------------------------------------------------------
    frame1 = tk.LabelFrame(root, text='Encode Text to Morse', fg='red', bg='black', font=('Arial', 14, 'bold'),
                           padx=15, pady=10)
    frame1.grid(row=0, column=0, padx=20, pady=10, sticky='E'+'W'+'N'+'S')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    txt1 = scrolledtext.ScrolledText(frame1, font=('Arial', 12), bg='black', fg='red',
                                     insertbackground='red', borderwidth=0)
    txt1.grid(row=0, column=0, sticky='E'+'W'+'N'+'S')
    txt1.focus()
    frame1.rowconfigure(0, weight=1)
    frame1.columnconfigure(0, weight=1)

    # FRAME2 inside FRAME1
    frame2 = tk.LabelFrame(frame1, bg='black', borderwidth=0)
    frame2.grid(row=1, column=0, sticky='E'+'W'+'N'+'S')

    # Buttons inside FRAME2
    button1 = tk.Button(frame2, text='ENCODE', anchor='w', padx=20, bg='black', fg='red', borderwidth=5,
                        command=lambda: code_gui(txt1, txt2))
    button1.grid(row=0, column=0, pady=(15, 0))
    frame2.rowconfigure(0, weight=1)
    frame2.columnconfigure(0, weight=1)

    button2 = tk.Button(frame2, text='EXPORT TO FILE', anchor='e', padx=6, bg='black', fg='red', borderwidth=5,
                        command=lambda: export_to_file(txt1))
    button2.grid(row=0, column=2, pady=(15, 0))
    frame2.columnconfigure(2, weight=1)

    # FRAME3 ----------------------------------------------------------------------------------------------------------

    frame3 = tk.LabelFrame(root, text='Decode Morse to Text', fg='red', bg='black', font=('Arial', 14, 'bold'),
                           padx=15, pady=10)
    frame3.grid(row=1, column=0, padx=20, pady=10, sticky='E' + 'W' + 'N' + 'S')
    root.rowconfigure(1, weight=1)

    txt2 = scrolledtext.ScrolledText(frame3, font=('Arial', 12), bg='black', fg='red',
                                     insertbackground='red', borderwidth=0)
    txt2.grid(row=0, column=0, sticky='E' + 'W' + 'N' + 'S')
    frame3.rowconfigure(0, weight=1)
    frame3.columnconfigure(0, weight=1)

    # FRAME4 inside FRAME3
    frame4 = tk.LabelFrame(frame3, bg='black', borderwidth=0)
    frame4.grid(row=1, column=0, sticky='E' + 'W' + 'N' + 'S')
    frame2.rowconfigure(1, weight=1)

    # Buttons inside FRAME4
    button3 = tk.Button(frame4, text='DECODE', anchor='w', padx=20, bg='black', fg='red', borderwidth=5,
                        command=lambda: decode_gui(txt2, txt1))
    button3.grid(row=0, column=0, pady=(15, 0))
    frame4.rowconfigure(0, weight=1)
    frame4.columnconfigure(0, weight=1)

    button4 = tk.Button(frame4, text='EXPORT TO FILE', anchor='e', padx=6, bg='black', fg='red', borderwidth=5,
                        command=lambda: export_to_file(txt2))
    button4.grid(row=0, column=2, pady=(15, 0))
    frame4.columnconfigure(2, weight=1)

    root.mainloop()


if __name__ == '__main__':
    if len(sys.argv) > 2:
        if sys.argv[1] == 'encode':
            if sys.argv[2] == 'terminal' or sys.argv[2] == 't':
                code(sys.argv[3], False)
            elif sys.argv[2] == 'file' or sys.argv[2] == 'f':
                code(sys.argv[3], True)
            else:
                print('Invalid output argument (argv[2]) -> specify output ("terminal"/"t" or "file"/"f")')
        elif sys.argv[1] == 'decode':
            if sys.argv[2] == 'terminal' or sys.argv[2] == 't':
                decode(sys.argv[3], False)
            elif sys.argv[2] == 'file' or sys.argv[2] == 'f':
                decode(sys.argv[3], True)
            else:
                print('Invalid output argument (argv[2]) -> specify output ("terminal"/"t" or "file"/"f")')
        else:
            print('Invalid action argument (argv[1]) -> specify action ("code" or "decode")')
    else:
        main()




