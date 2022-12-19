from download import start_psx, start_psp, start_ps2, start

if __name__ == "__main__":

    # start here
    # execute download threads
    # examples
    #start_ps2(is_threaded=True, number_threads=5, output_file_path="")
    #start_psx(is_threaded=False, number_threads=0, output_file_path="/media/uzer/E7DD-60A5/emulation/consoles/psx/")
    #start_psp(is_threaded=True, number_threads=5, output_file_path="/media/uzer/E7DD-60A5/emulation/consoles/psp/")

    start(url="https://archive.org/download/En-ROMs/En-ROMs/Sony%20-%20PlayStation%202%20%5BT-En%5D%20Collection/",
          file_ext=".7z",
          is_threaded=True,
          number_threads=5,
          output_file_path="/media/uzer/E7DD-60A5/emulation/consoles/ps2/translations/")
