import os
import zipfile


def extract(folder):
    filename = '{}.zip'.format(folder)
    print('Extracting {}...'.format(filename))
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall('data')


def main():
    ''' Main function '''

    if not os.path.isdir('《刘慈欣作品全集》(v1.0)'):
        extract('《刘慈欣作品全集》(v1.0)')


if __name__ == '__main__':
    main()
