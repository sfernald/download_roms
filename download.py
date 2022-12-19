import os
import urllib3
import threading
from bs4 import BeautifulSoup
from urllib.parse import unquote


# get this page https://archive.org/details/@millikesse
# print this list of href urls in a element
# get download page of each and
# then get all the .chd file links each page
# and finally download all the .chd files

def start_threaded(download_roms, number_threads, output_file_path) -> bool:

    # got the list, now download the files using threads
    # pop x entries off list
    # create a thread for each entry
    # run download_file procedure on each thread
    while download_roms:
        if len(download_roms) > number_threads:
            rom_queue, download_roms = download_roms[:number_threads], download_roms[number_threads:]
        else:
            rom_queue = download_roms
            download_roms = []

        threads = []
        for url, filename in rom_queue:
            t = threading.Thread(target=download_file, args=(url, filename, output_file_path))
            threads.append(t)

        for x in threads:
            x.start()

        # wait for all threads to finish
        for x in threads:
            x.join()

    return True


# all download logic extracted to this procedure
def download_file(url, filename, output_file_path) -> bool:
    req = urllib3.PoolManager()

    input_file = url + '/' + filename
    print(input_file)

    output_file = output_file_path + unquote(filename)

    try:
        if not os.path.exists(output_file):
            resp = req.request('GET', input_file)
            f = open(output_file, 'wb')
            f.write(resp.data)
            f.close()
            resp.release_conn()
        else:
            print(output_file + " already exists.")
            return False
    except Exception as e:
        print(e)
        print("Could not download file.")
        return False

    return True


def get_file_list(url, file_ext) -> []:
    download_roms = []

    req = urllib3.PoolManager()

    res = req.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')
    for link in soup.find_all('a'):
        dl_str = str(link.get('href')).rstrip('/')
        if dl_str.find(file_ext) != -1:
            if (url, dl_str) not in download_roms:
                print(dl_str)
                download_roms.append((url, dl_str))

    return download_roms


# this scrapes up all the .chd files across all the web pages and puts them in an array for later processing
def scrape_file_list_ps2() -> []:
    download_roms = []

    req = urllib3.PoolManager()

    dl = "https://archive.org/download/"
    url = "https://archive.org/details/@millikesse"

    res = req.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')

    for link in soup.find_all('a'):
        link_str = str(link.get('href'))
        if link_str.find('ps2-redump-usa') != -1:
            dl_url = dl + link_str[9:]
            print(dl + link_str[9:])
            res_dl = req.request('GET', dl_url)
            soup_dl = BeautifulSoup(res_dl.data, 'html.parser')
            for link_dl in soup_dl.find_all('a'):
                dl_str = str(link_dl.get('href'))
                if dl_str.find('.chd') != -1 and dl_str.find('.xml') == -1:
                    print(dl_str)
                    download_roms.append((dl_url, dl_str))

    return download_roms


# this will scrape for all the .chd files and then download all that it finds that aren't already downloaded
def start_ps2(is_threaded, number_threads, output_file_path) -> bool:

    # scrape file list
    download_roms = scrape_file_list_ps2()

    # got the list, now download the files
    if is_threaded:
        start_threaded(download_roms, number_threads, output_file_path)
    else:
        for url, filename in download_roms:
            download_file(url, filename, output_file_path)

    return True


# this will scrape for all the rom files and then download all that it finds that aren't already downloaded
def start_psx(is_threaded, number_threads, output_file_path) -> bool:

    # scrape file list
    url = 'https://archive.org/download/rr-sony-playstation-u/usa/'
    file_ext = '.7z'
    download_roms = get_file_list(url, file_ext)

    # got the list, now download the files
    if is_threaded:
        start_threaded(download_roms, number_threads, output_file_path)
    else:
        for url, filename in download_roms:
            download_file(url, filename, output_file_path)

    return True


# this will scrape for all the rom files and then download all that it finds that aren't already downloaded
def start_psp(is_threaded, number_threads, output_file_path) -> bool:

    # scrape file list
    url = 'https://archive.org/download/rr-sony-playstation-portable/usa/'
    file_ext = '.7z'
    download_roms = get_file_list(url, file_ext)

    # got the list, now download the files
    if is_threaded:
        start_threaded(download_roms, number_threads, output_file_path)
    else:
        for url, filename in download_roms:
            download_file(url, filename, output_file_path)

    return True

# this will scrape for all the rom files and then download all that it finds that aren't already downloaded
def start(url, file_ext, is_threaded, number_threads, output_file_path) -> bool:

    # scrape file list
    download_roms = get_file_list(url, file_ext)

    # got the list, now download the files
    if is_threaded:
        start_threaded(download_roms, number_threads, output_file_path)
    else:
        for url, filename in download_roms:
            download_file(url, filename, output_file_path)

    return True



